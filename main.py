import json
import os
from product import Product
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
            {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
            {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
            {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
        ]

    inventory = Inventory()         
    for item in data:
        product = Product(item["id"], item["name"], item["price"], item["stock"])
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
        id = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        product = Product(id, name, price, stock)
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