import unittest

from supplier import Supplier
from product_factory import ProductFactory
from order import Order
from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount


class TestDiscountStrategies(unittest.TestCase):
    def setUp(self) -> None:
        supplier = Supplier("S001", "TechWorld", "sales@techworld.com")
        self.chair = ProductFactory.create("physical", "P010", "Chair", 125.00, 10, supplier, weight=12.0)

    def make_order(self, discount=None) -> Order:
        order = Order("O001", discount)
        order.add_order_line(self.chair, 2)  # subtotal 250.00
        return order

    def test_no_discount_returns_total_unchanged(self) -> None:
        self.assertEqual(NoDiscount().apply(100.0), 100.0)

    def test_percentage_discount(self) -> None:
        self.assertAlmostEqual(PercentageDiscount(10).apply(250.0), 225.0)

    def test_bulk_discount_applies_at_threshold(self) -> None:
        self.assertEqual(BulkDiscount(200, 20).apply(200.0), 180.0)

    def test_bulk_discount_not_applied_below_threshold(self) -> None:
        self.assertEqual(BulkDiscount(200, 20).apply(199.99), 199.99)

    def test_student_discount_is_five_percent(self) -> None:
        self.assertAlmostEqual(StudentDiscount().apply(100.0), 95.0)

    def test_order_defaults_to_no_discount(self) -> None:
        self.assertAlmostEqual(self.make_order().calculate_total(), 250.0)

    def test_order_uses_bulk_discount(self) -> None:
        self.assertAlmostEqual(self.make_order(BulkDiscount(200, 20)).calculate_total(), 230.0)

    def test_set_discount_changes_strategy(self) -> None:
        order = self.make_order(BulkDiscount(200, 20))
        order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(order.calculate_total(), 225.0)

    def test_invalid_percentage_rejected(self) -> None:
        with self.assertRaises(ValueError):
            PercentageDiscount(150)


if __name__ == "__main__":
    unittest.main()
