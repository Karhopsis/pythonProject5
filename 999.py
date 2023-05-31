class House:

def __init__(self, price, area):

    self.price = price

    self.area = area

    def __str__(self):

    return f"House price: {self.price}, area: {self.area} m2"

class SmallHouse(House):

    def __init__(self, price):

    super().__init__(price, 50)

    class Human:

    def __init__(self, name, age, money):

    self.name = name

    self.age = age

    self.money = money

    self.house = None

    def earn_money(self, amount):

    self.money += amount

    def buy_house(self, house):

    if self.money >= house.price:

    self.money -= house.price

    self.house = house

    print(f"{self.name} has bought a house!")

    print(f"{self.name} has {self.money} dollars left")

    else:

print(f"{self.name} does not have enough money to buy the house")

# Пример использования классов и методов

if __name__ == '__main__':

house1 = SmallHouse(100000)

house2 = House(500000, 100)

person1 = Human("John", 30, 100000)

person2 = Human("Mary", 25, 50000)

person1.buy_house(house1)

person2.buy_house(house2)