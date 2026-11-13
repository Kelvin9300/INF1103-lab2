import json
import os
from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

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
    if item["type"] == "physical":
        return PhysicalProduct(item["id"], item["name"], item["price"], item["stock"],
                               supplier, item["weight"])
    return DigitalProduct(item["id"], item["name"], item["price"], item["stock"],
                          supplier, item["download_size"])


def load_inventory() -> Inventory:
    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        with open("inventory.json", "r") as file:
            data = json.load(file)
        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found. Starting with default inventory.")
        software_supplier = {"supplier_id": "S002", "name": "SoftHub",
                             "contact_email": "hello@softhub.com"}
        data = [
            {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15,
             "supplier": DEFAULT_SUPPLIER, "type": "physical", "weight": 2.0},
            {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40,
             "supplier": DEFAULT_SUPPLIER, "type": "physical", "weight": 0.5},
            {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25,
             "supplier": DEFAULT_SUPPLIER, "type": "physical", "weight": 0.8},
            {"id": "P004", "name": "Antivirus Licence", "price": 49.90, "stock": 100,
             "supplier": software_supplier, "type": "digital", "download_size": 350}
        ]

    inventory = Inventory()
    for item in data:
        inventory.add_product(create_product(item))
    return inventory


def save_inventory(inventory: Inventory) -> None:
    data = [product.to_dict() for product in inventory.get_products()]
    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)


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
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        supplier_id = input("Supplier ID: ")
        if supplier_id in suppliers:
            supplier = suppliers[supplier_id]
            print(f"Using existing supplier: {supplier.get_name()}")
        else:
            supplier_name = input("Supplier Name: ")
            supplier_email = input("Supplier Email: ")
            supplier = get_or_create_supplier({"supplier_id": supplier_id, "name": supplier_name,
                                               "contact_email": supplier_email})

        if product_type == "physical":
            weight = float(input("Weight (kg): "))
            product = PhysicalProduct(id, name, price, stock, supplier, weight)
        else:
            download_size = float(input("Download Size (MB): "))
            product = DigitalProduct(id, name, price, stock, supplier, download_size)
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
            new_stock = int(input("New Stock Quantity: "))
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
