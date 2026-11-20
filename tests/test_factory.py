import unittest

from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory


class TestProductFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier("S001", "TechWorld", "sales@techworld.com")

    def test_creates_physical_product(self) -> None:
        product = ProductFactory.create("physical", "P001", "Lamp", 25.0, 10, self.supplier, weight=1.0)
        self.assertIsInstance(product, PhysicalProduct)
        self.assertIsInstance(product, Product)

    def test_creates_digital_product(self) -> None:
        product = ProductFactory.create("digital", "D001", "Editor", 49.9, 100, self.supplier, download_size=800)
        self.assertIsInstance(product, DigitalProduct)

    def test_unknown_type_raises_clear_value_error(self) -> None:
        with self.assertRaises(ValueError) as context:
            ProductFactory.create("service", "S001", "Install", 30.0, 5, self.supplier)
        self.assertIn("Unknown product type: service", str(context.exception))


if __name__ == "__main__":
    unittest.main()
