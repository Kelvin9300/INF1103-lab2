import json
import os
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        with open("inventory.json", "r") as file:
            data = json.load(file)
        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found. Starting with default inventory.")
        data = [
            {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15, "type": "physical", "weight": 2.0},
            {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40, "type": "physical", "weight": 0.5},
            {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25, "type": "physical", "weight": 0.8},
            {"id": "P004", "name": "Antivirus Licence", "price": 49.90, "stock": 100, "type": "digital", "download_size": 350},
        ]

    inventory = Inventory()         
    for item in data:
        if item["type"] == "physical":
            product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item["weight"])
        else:
            product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item["download_size"])
        inventory.add_product(product)
    return inventory

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump([product.to_dict() for product in inventory.get_products()], file, indent=4)

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
        if product_type == "physical":
            weight = float(input("Weight (kg): "))
            product = PhysicalProduct(id, name, price, stock, weight)
        elif product_type == "digital":
            download_size = float(input("Download Size (MB): "))
            product = DigitalProduct(id, name, price, stock, download_size)
        else:
            print("Invalid product type. Product not added.")
            continue
        inventory.add_product(product)
        print("Product added successfully!")
    elif choice == "3":
        print("Update Stock")
        id = input("Enter Product ID: ")
        product = inventory.search_product(id)
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
        product = inventory.search_product(id)
        if product is not None:
            print("Product Found")
            print("-" * 48)
            print(f"ID: {product.get_product_id()}")
            print(f"Name: {product.get_name()}")
            print(f"Price: ${product.get_price():.2f}")
            print(f"Stock: {product.get_stock()}")
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