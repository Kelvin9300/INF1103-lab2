import json
import os


def display_all(inventory):
    
    print("Current Inventory")
    print("-" * 48)
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("-" * 48)

def add_product(inventory, id, name, price, stock):
    new_product = {"id": id, "name": name, "price": price, "stock": stock}
    inventory.append(new_product)

def search_product(inventory, id):
    for product in inventory:
        if product["id"] == id:
            return product
    return None

def update_stock(inventory, id, new_stock):
    product = search_product(inventory, id)
    if product is not None:
        product["stock"] = new_stock
        return True
    return False

def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        with open("inventory.json", "r") as file:
            data = json.load(file)
        print("Inventory loaded successfully.")
        return data
    else:
        print("inventory.json not found. Starting with default inventory.")
        return [
            {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
            {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
            {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
        ]

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)
        
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
        display_all(inventory)
    elif choice == "2":
        print("Add New Product")
        id = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        add_product(inventory, id, name, price, stock)
        print("Product added successfully!")
    elif choice == "3":
        print("Update Stock")
        id = input("Enter Product ID: ")
        product = search_product(inventory, id)
        if product is not None:
            print("Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")
            new_stock = int(input("New Stock Quantity: "))
            update_stock(inventory, id, new_stock)
            print("Stock updated successfully!")
        else:
            print("Product not found.")
    elif choice == "4":
        print("Search Product")
        id = input("Enter Product ID: ")
        product = search_product(inventory, id)
        if product is not None:
            print("Product Found")
            print("-" * 48)
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
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