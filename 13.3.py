class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def change_kg(self):
        return self.__kg
    @change_kg.setter
    def change_kg(self,new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            print('Килограммы задаются только числами')


date = KgToPounds(12)
date.change_kg = 20
print()