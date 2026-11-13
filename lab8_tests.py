from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def test_association() -> None:
    print("=== Section 2: Association (Supplier - Product) ===")
    supplier = Supplier("S001", "TechWorld", "sales@techworld.com")
    guitar = PhysicalProduct("P006", "Guitar", 350.00, 5, supplier, 4.5)
    ebook = DigitalProduct("P007", "E-Book", 10.00, 20, supplier, 20.0)

    print("Supplier through each product:")
    guitar.get_supplier().display_information()
    ebook.get_supplier().display_information()
    print("Both products share the same Supplier object:", guitar.get_supplier() is ebook.get_supplier())

    del supplier
    print("After 'del supplier', products still reach their supplier:")
    guitar.get_supplier().display_information()
    ebook.get_supplier().display_information()
    print()


def test_aggregation() -> None:
    print("=== Section 3: Aggregation (Inventory - Product) ===")
    supplier = Supplier("S001", "TechWorld", "sales@techworld.com")
    laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, supplier, 2.0)
    print("Product created before any inventory exists:")
    laptop.display_information()

    inventory_a = Inventory()
    inventory_b = Inventory()
    inventory_a.add_product(laptop)
    print("Added to Inventory A. Found in A:", inventory_a.find_product("P001") is laptop)

    removed = inventory_a.remove_product("P001")
    print("Removed from Inventory A. Found in A:", inventory_a.find_product("P001"))
    print("Removed product is the same object:", removed is laptop)
    print("Product still works after removal:")
    print("update_stock(20):", laptop.update_stock(20))
    laptop.display_information()

    inventory_b.add_product(laptop)
    print("Added same object to Inventory B. Found in B:", inventory_b.find_product("P001") is laptop)
    print()


def test_composition() -> None:
    print("=== Section 4: Composition (Order - OrderLine) ===")
    supplier = Supplier("S001", "TechWorld", "sales@techworld.com")
    mouse = PhysicalProduct("P002", "Mouse", 25.50, 40, supplier, 0.5)
    licence = DigitalProduct("P004", "Antivirus Licence", 49.90, 100, supplier, 350)

    order1 = Order("O001")
    order1.add_order_line(mouse, 2)
    order1.add_order_line(licence, 1)
    order1.display_order()

    order2 = Order("O002")
    order2.add_order_line(mouse, 3)
    order2.display_order()

    line1 = order1.get_order_lines()[0]
    line2 = order2.get_order_lines()[0]
    print("Same Product object in both orders:", line1.get_product() is line2.get_product())
    print("Same OrderLine object in both orders:", line1 is line2)
    print("Product id:", id(line1.get_product()), id(line2.get_product()))
    print("OrderLine id:", id(line1), id(line2))

    print("Removing Mouse line from O001:", order1.remove_order_line("P002"))
    order1.display_order()
    print("Mouse product still exists:", mouse.get_name())
    print()


def test_lsp_and_polymorphism() -> None:
    print("=== Sections 6-7: LSP and Polymorphism ===")
    supplier = Supplier("S001", "TechWorld", "sales@techworld.com")
    keyboard = PhysicalProduct("P003", "Keyboard", 45.00, 25, supplier, 0.8)
    licence = DigitalProduct("P004", "Antivirus Licence", 49.90, 100, supplier, 350)

    print("show_product_details() with each subclass:")
    show_product_details(keyboard)
    show_product_details(licence)

    print("update_stock() keeps the same meaning for both subclasses:")
    for product in [keyboard, licence]:
        print(product.get_name(), "update_stock(10):", product.update_stock(10),
              "| update_stock(-1):", product.update_stock(-1), "| stock:", product.get_stock())

    inventory = Inventory()
    inventory.add_product(keyboard)
    inventory.add_product(licence)
    print("One loop over list[Product], no isinstance checks:")
    for product in inventory.get_products():
        product.display_information()
        print(product.get_fulfilment_info())

    try:
        Product("P999", "Generic", 1.00, 1, supplier)
    except TypeError as e:
        print("Abstract Product cannot be created:", e)


if __name__ == "__main__":
    test_association()
    test_aggregation()
    test_composition()
    test_lsp_and_polymorphism()
