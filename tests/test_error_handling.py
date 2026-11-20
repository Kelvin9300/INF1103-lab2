import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from supplier import Supplier
from inventory import Inventory
from input_helpers import get_positive_float
from product_loader import load_products

CSV_CONTENT = """product_type,product_id,name,price,stock_quantity
physical,P001,Desk Lamp,25.00,10
digital,D001,Photo Editor,49.90,100
service,S001,Installation,30.00,5
physical,P002,Office Chair,abc,3
physical,P003,Monitor Stand,39.50,7
"""


class TestErrorHandling(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier("S001", "TechWorld", "sales@techworld.com")

    def test_get_positive_float_asks_again_until_valid(self) -> None:
        output = io.StringIO()
        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]), redirect_stdout(output):
            value = get_positive_float("Price: ")
        self.assertEqual(value, 12.5)
        self.assertIn("Please enter a valid number", output.getvalue())
        self.assertIn("greater than zero", output.getvalue())

    def test_load_products_skips_bad_rows(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "products.csv")
            with open(path, "w", newline="") as file:
                file.write(CSV_CONTENT)
            inventory = Inventory()
            output = io.StringIO()
            with redirect_stdout(output):
                load_products(path, inventory, self.supplier)
        loaded_ids = [p.get_product_id() for p in inventory.get_products()]
        self.assertEqual(loaded_ids, ["P001", "D001", "P003"])
        self.assertIn("3 products loaded.", output.getvalue())
        self.assertIn("Load attempt finished.", output.getvalue())

    def test_missing_file_handled_gracefully(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            load_products("does_not_exist.csv", Inventory(), self.supplier)
        self.assertIn("Products file not found", output.getvalue())
        self.assertIn("Load attempt finished.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
