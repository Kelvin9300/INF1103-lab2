"""Lab 9 demo: run each Predict First scenario and print what happens."""
from unittest.mock import patch

from supplier import Supplier
from product_factory import ProductFactory
from inventory import Inventory
from order import Order
from order_line import OrderLine
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount
from input_helpers import get_positive_float
from product_loader import load_products

supplier = Supplier("S001", "TechWorld", "sales@techworld.com")

print("=== Section 2: Strategy pattern ===")
chair = ProductFactory.create("physical", "P010", "Ergonomic Chair", 125.00, 10, supplier, weight=12.0)
order = Order("O001", BulkDiscount(200, 20))
order.add_order_line(chair, 2)  # 2 x 125.00 = 250.00
print(f"Subtotal 250.00 with BulkDiscount(200, 20): {order.calculate_total():.2f}")
order.set_discount(PercentageDiscount(10))
print(f"Same order after set_discount(PercentageDiscount(10)): {order.calculate_total():.2f}")
order.set_discount(StudentDiscount())
print(f"Same order with StudentDiscount (new class, Order unchanged): {order.calculate_total():.2f}")
shared = PercentageDiscount(10)
order_a = Order("O002", shared)
order_b = Order("O003", shared)
print("Two orders can share one strategy object:", order_a.get_discount() is order_b.get_discount())
print()

print("=== Section 3: Factory pattern ===")
lamp = ProductFactory.create("physical", "P001", "Desk Lamp", 25.00, 10, supplier, weight=1.2)
editor = ProductFactory.create("digital", "D001", "Photo Editor", 49.90, 100, supplier, download_size=800)
for product in [lamp, editor]:
    print(type(product).__name__, "->", product.get_fulfilment_info())
try:
    ProductFactory.create("service", "S001", "Installation", 30.00, 5, supplier)
except ValueError as e:
    print("ValueError caught:", e)
print()

print("=== Section 4: Validation ===")
tests = [
    ("price 0", lambda: ProductFactory.create("physical", "X1", "Bad", 0, 5, supplier)),
    ("stock -1", lambda: ProductFactory.create("digital", "X2", "Bad", 10.0, -1, supplier)),
    ("quantity 0", lambda: OrderLine(lamp, 0)),
]
for label, action in tests:
    try:
        action()
    except ValueError as e:
        print(f"Rejected {label}: {e}")
print()

print("=== Section 5.1: get_positive_float with inputs abc, -5, 12.50 ===")
with patch("builtins.input", side_effect=["abc", "-5", "12.50"]):
    value = get_positive_float("Price: ")
print("Returned value:", value)
print()

print("=== Section 5.2: load_products with products.csv ===")
inventory = Inventory()
load_products("products.csv", inventory, supplier)
inventory.display_all()
print()

print("=== Section 5.2: load_products with a missing file ===")
load_products("missing_products.csv", Inventory(), supplier)
