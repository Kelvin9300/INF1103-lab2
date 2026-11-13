from product import Product


class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []  # aggregation: holds references, does not own them

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> Product | None:
        product = self.find_product(product_id)
        if product is not None:
            self.__products.remove(product)  # removes the reference only; the object still exists
        return product

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self) -> None:
        print("Current Inventory")
        print("-" * 48)
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    def get_products(self) -> list[Product]:
        return list(self.__products)


if __name__ == "__main__":
    from supplier import Supplier
    from physical_product import PhysicalProduct
    from digital_product import DigitalProduct
    s = Supplier("S001", "TechWorld", "sales@techworld.com")
    inv = Inventory()
    inv.add_product(PhysicalProduct("P001", "Laptop", 1200.00, 15, s, 2.0))
    inv.add_product(DigitalProduct("P002", "Antivirus Licence", 49.90, 100, s, 350))
    inv.display_all()
    print(inv.find_product("P002").get_name())
    print(inv.find_product("P999"))
