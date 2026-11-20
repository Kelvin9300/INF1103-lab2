import json
import os
from supplier import Supplier
from product import Product
from product_factory import ProductFactory
from inventory import Inventory
from input_helpers import get_positive_float, get_non_negative_int

DEFAULT_SUPPLIER: dict[str, str] = {
    "supplier_id": "S001", "name": "TechWorld", "contact_email": "sales@techworld.com"
}

# One Supplier object per supplier ID, shared by all its products (association)
suppliers: dict[str, Supplier] = {}


def get_or_create_supplier(data: dict[str, str]) -> Supplier:
    supplier_id = data["supplier_id"]
    if supplier_id not in suppliers:
        suppliers[supplier_id] = Supplier(supplier_id, data["name"], data["contact_email"])
    return suppliers[supplier_id]


def create_product(item: dict) -> Product:
    # Older saves have no supplier, so fall back to the default supplier
    supplier = get_or_create_supplier(item.get("supplier", DEFAULT_SUPPLIER))
    return ProductFactory.create(item["type"], item["id"], item["name"], item["price"],
                                 item["stock"], supplier,
                                 weight=item.get("weight", 0.0),
                                 download_size=item.get("download_size", 0.0))


def default_data() -> list[dict]:
    software_supplier = {"supplier_id": "S002", "name": "SoftHub",
                         "contact_email": "hello@softhub.com"}
    return [
        {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15,
         "supplier": DEFAULT_SUPPLIER, "type": "physical", "weight": 2.0},
        {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40,
         "supplier": DEFAULT_SUPPLIER, "type": "physical", "weight": 0.5},
        {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25,
         "supplier": DEFAULT_SUPPLIER, "type": "physical", "weight": 0.8},
        {"id": "P004", "name": "Antivirus Licence", "price": 49.90, "stock": 100,
         "supplier": software_supplier, "type": "digital", "download_size": 350}
    ]


def load_inventory() -> Inventory:
    data: list[dict]
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("inventory.json not found. Starting with default inventory.")
        data = default_data()
    except json.JSONDecodeError:
        print("inventory.json is damaged. Starting with default inventory.")
        data = default_data()
    else:
        print("inventory.json found.")
        print("Inventory loaded successfully.")

    inventory = Inventory()
    for item in data:
        try:
            inventory.add_product(create_product(item))
        except (KeyError, ValueError) as e:
            print(f"Skipped invalid product {item.get('id', '?')}: {e}")
    return inventory


def save_inventory(inventory: Inventory) -> None:
    data = [product.to_dict() for product in inventory.get_products()]
    try:
        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)
    except OSError as e:
        print(f"Could not save inventory: {e}")


print("=" * 40)
print("INVENTORY MANAGEMENT SYSTEM")
print("=" * 40)

inventory = load_inventory()

while True:
    print()
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
    choice = input("Enter option: ")

    if choice == "1":
        inventory.display_all()
    elif choice == "2":
        print("Add New Product")
        product_type = input("Product type (physical/digital): ").lower()
        if product_type not in ("physical", "digital"):
            print("Invalid product type. Product not added.")
            continue
        id = input("Product ID: ")
        name = input("Product Name: ")
        price = get_positive_float("Price: ")
        stock = get_non_negative_int("Stock Quantity: ")

        supplier_id = input("Supplier ID: ")
        if supplier_id in suppliers:
            supplier = suppliers[supplier_id]
            print(f"Using existing supplier: {supplier.get_name()}")
        else:
            supplier_name = input("Supplier Name: ")
            supplier_email = input("Supplier Email: ")
            supplier = get_or_create_supplier({"supplier_id": supplier_id, "name": supplier_name,
                                               "contact_email": supplier_email})

        weight = 0.0
        download_size = 0.0
        if product_type == "physical":
            weight = get_positive_float("Weight (kg): ")
        else:
            download_size = get_positive_float("Download Size (MB): ")

        try:
            product = ProductFactory.create(product_type, id, name, price, stock, supplier,
                                            weight=weight, download_size=download_size)
        except ValueError as e:
            print(f"Product not added: {e}")
            continue
        inventory.add_product(product)
        print("Product added successfully!")
    elif choice == "3":
        print("Update Stock")
        id = input("Enter Product ID: ")
        product = inventory.find_product(id)
        if product is not None:
            print("Product Found:")
            print(f"Name: {product.get_name()}")
            print(f"Current Stock: {product.get_stock()}")
            new_stock = get_non_negative_int("New Stock Quantity: ")
            if product.update_stock(new_stock):
                print("Stock updated successfully!")
            else:
                print("Invalid stock quantity. Update failed.")
        else:
            print("Product not found.")
    elif choice == "4":
        print("Search Product")
        id = input("Enter Product ID: ")
        product = inventory.find_product(id)
        if product is not None:
            print("Product Found")
            print("-" * 48)
            product.display_information()
            print(product.get_fulfilment_info())
            product.get_supplier().display_information()
            print("-" * 48)
        else:
            print("Product not found.")
    elif choice == "5":
        print("Saving inventory...")
        save_inventory(inventory)
        print("Inventory saved successfully to inventory.json.")
    elif choice == "6":
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Inventory saved successfully.")
        print()
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("Invalid option. Please try again.")
