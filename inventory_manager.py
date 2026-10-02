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

inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
]

display_all(inventory)