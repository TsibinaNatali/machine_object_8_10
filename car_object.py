import random

class NegativePriceError(Exception):
    pass
class Car:
    def __init__(self,brand,color,price,owner):
        if price < 0:
            raise NegativePriceError(f"Нельзя создать машину {brand} с отрицательной стоимостью")
        self.brand =brand
        self.color = color
        self.price = price
        self.owner = owner
        self._number = random.randint(100,999)

    @property
    def number(self):
        return self._number

    def newColor(self,new_color):
        self.color = new_color

    def newOwner(self,new_owner):
        self.owner = new_owner
    def newPrice(self,new_price):
        if new_price < 0:
            raise NegativePriceError (f"стоимость машины {self.brand} не может быть отрицательной")
        else:
            self.price = new_price

    def infoCar(self):
        return f"Машина - {self.brand} №{self._number}\nЦвет машины - {self.color}\nЦена машины = {self.price}\nИмя владельца -{self.owner}"

# создаем машины
try:
    car1 = Car("Lada","Белая",300000,"Олег")
    car2 = Car("BMW X5","Черный",8500000,"Мария")

    print(car1.infoCar())
    print()
    print(car2.infoCar())
except NegativePriceError as e:
    print(f"ошибка{e}")
print()
try:
    car1.newPrice(350000)
    car1.newColor("синий")
    car1.newOwner("Игорь")

    print(car1.infoCar())
except NegativePriceError as e:
    print(f"ошибка{e}")