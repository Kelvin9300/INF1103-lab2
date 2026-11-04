from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def calculate_shipping_cost(self):
        return self.__weight * 10  # Example: $10 per kg

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

if __name__ == "__main__":
    p = PhysicalProduct("P006", "Guitar", 350.00, 5, 4.5)
    p.display_information()
    print(p.get_name())
    print(p.get_weight())
    print(p.update_stock(8))
    print(p.get_fulfilment_info())

    light = PhysicalProduct("P008", "USB Cable", 9.90, 50, 0.2)
    print(f"Shipping for {p.get_name()}: ${p.calculate_shipping_cost():.2f}")
    print(f"Shipping for {light.get_name()}: ${light.calculate_shipping_cost():.2f}")
    print(p.to_dict())