class Soda():
    def __init__(self,add):
        if isinstance(add,str):
            self.add = add
        else:
            self.add = None

    def show_my_drink(self):
        if self.add:
            return 'Soda with: '+self.add
        else:
            return 'Default soda'


e = Soda('')

print(e.show_my_drink())
