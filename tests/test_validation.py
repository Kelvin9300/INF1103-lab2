import unittest

from supplier import Supplier
from product_factory import ProductFactory
from order_line import OrderLine


class TestValidation(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier("S001", "TechWorld", "sales@techworld.com")
        self.lamp = ProductFactory.create("physical", "P001", "Lamp", 25.0, 10, self.supplier, weight=1.0)

    def test_price_must_be_positive(self) -> None:
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P002", "Bad", 0, 5, self.supplier)

    def test_stock_cannot_be_negative(self) -> None:
        with self.assertRaises(ValueError):
            ProductFactory.create("digital", "D002", "Bad", 10.0, -1, self.supplier)

    def test_order_line_quantity_must_be_positive(self) -> None:
        with self.assertRaises(ValueError):
            OrderLine(self.lamp, 0)

    def test_valid_order_line_is_created(self) -> None:
        self.assertEqual(OrderLine(self.lamp, 2).calculate_subtotal(), 50.0)


if __name__ == "__main__":
    unittest.main()
