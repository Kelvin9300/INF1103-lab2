from product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")
    
    def get_fulfilment_info(self):
        return "This product will be delivered digitally."
    
if __name__ == "__main__":
    d = DigitalProduct("P007", "Antivirus Licence", 49.90, 100, 350)
    d.display_information()
    print(d.get_name())
    print(d.get_download_size())
    print(d.get_fulfilment_info())