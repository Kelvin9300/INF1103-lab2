from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, download_size: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self) -> str:
        return "This product will be delivered digitally."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data


if __name__ == "__main__":
    from can_be_shipped import CanBeShipped
    s = Supplier("S002", "SoftHub", "hello@softhub.com")
    d = DigitalProduct("P007", "Antivirus Licence", 49.90, 100, s, 350)
    d.display_information()
    print(d.get_fulfilment_info())
    print(isinstance(d, CanBeShipped))
    print(d.to_dict())
