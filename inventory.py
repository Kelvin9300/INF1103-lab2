class Inventory:
    def __init__(self):
        self.__products = []          

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:                 
            if product.get_product_id() == product_id:           
                return product
        return None                         

    def display_all(self):
        print("Current Inventory")
        print("-" * 48)
        for product in self.__products:                 
            product.display_information()                            
        print("-" * 48)

    def get_products(self):
        return self.__products                          


if __name__ == "__main__":
    from product import Product
    inv = Inventory()
    inv.add_product(Product("P001", "Laptop", 1200.00, 15))
    inv.add_product(Product("P002", "Mouse", 25.50, 40))
    inv.display_all()
    print(inv.search_product("P002").get_name())
    print(inv.search_product("P999"))