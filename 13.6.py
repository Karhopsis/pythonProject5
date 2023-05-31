class Human():
    default_name = "Vasil"
    default_age = 26
    def __init__(self, name = default_name, age = default_age):
        self.age = age
        self.name = name
        self._money = 30000.0
        self._house = "Default house"

    def info(self):
        return self.name, self.age, self._money, self._house
    @staticmethod
    def default_info():
        return Human.default_name, Human.default_age

    def make_deal(self, house1, price):
        if type(house1) != str or type(price) != float:
            raise TypeError("Wrong type")

        self._money = self._money - price
        self._house = house1

    def earn_money(self, erned_money):
        self._money = self._money + erned_money

    def buy_house(self,house1,price):
        self.make_deal(house1,price)
        if self._money <0:
            raise TypeError("Not enough money")
        return self._money, self._house, "Accepted"

class House():
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self,sale):
        self._price = self._price - sale
        return self._price


class SmallHouse(House):
    def __init__(self):
        House.__init__(self, 40, 26000.0)

def main():
    p = Human()
    print(p.default_info())
    print(p.info())
    s = SmallHouse()
    print(p.buy_house('House1',s.final_price(1000)))



main()














