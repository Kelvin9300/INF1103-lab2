from product import Product

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

if __name__ == "__main__":
    p = PhysicalProduct("P006", "Guitar", 350.00, 5, 4.5)
    p.display_information()
    print(p.get_name())
    print(p.get_weight())
    print(p.update_stock(8))
    print(p.get_fulfilment_info())