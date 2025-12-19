class Product:
    def __init__(self, name):
        self.name = name 
        self.__price = 0  
        self.__discount = 0       

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Narx manfiy bo‘lishi mumkin emas!")

    def apply_discount(self, percent):
        if 0 <= percent <= 100:
            self.__discount = percent
        else:
            print("Chegirma 0-100 oralig‘ida bo‘lishi kerak!")

    def get_final_price(self):
        return self.__price * (1 - self.__discount / 100)


product = Product("Telefon")

product.set_price(5_000_000)
product.apply_discount(10)

print("Yakuniy narx:", product.get_final_price())
