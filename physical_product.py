from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, weight: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight

    def get_weight(self) -> float:
        return self.__weight

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 10  # $10 per kg

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data


if __name__ == "__main__":
    s = Supplier("S001", "TechWorld", "sales@techworld.com")
    p = PhysicalProduct("P006", "Guitar", 350.00, 5, s, 4.5)
    p.display_information()
    print(p.get_fulfilment_info())
    print(f"Shipping for {p.get_name()}: ${p.calculate_shipping_cost():.2f}")
    print(p.to_dict())
