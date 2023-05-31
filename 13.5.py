class Tomato:
    tomatos = []
    states = ['Blooming','Green','Red']
    def __init__(self,index):
            self._index = index
            self._state = self.states[0]
            TomatoBush.tomatos.append(self._index)
            TomatoBush.tomatos.append(self._state)

    def grow(self):
        for i in range(len(self.tomatos)):
            if self.tomatos[i] in self.states:
                if self.tomatos[i] == self.states[0]:
                    self.tomatos[i] = self.states[1]
                elif self.tomatos[i] == self.states[1]:
                    self.tomatos[i] = self.states[2]
                else:
                    return 'Grown'

        return self.tomatos

    def is_ripe(self):
        if self._state == 'Red':
            return 'Already grown'
        else:
            return self._state

    def give_away_all(self):
        self.tomatos = []

class TomatoBush(Tomato):

    def __init__(self,n):
        self.n = n
        for i in range(self.n):
            super().__init__(i+1)

    def gets(self):
        return self.tomatos

    def all_are_ripe(self):
        for i in range(len(self.tomatos)):
            if self.tomatos[i] in self.states:
                if type(self.tomatos[i]) in (float,int) or self.tomatos[i] == 'Red':
                    return True
                else:
                    return False



class Gardener(Tomato):

    def __init__(self,name):
        self._plant = TomatoBush(3)
        self.name = name

    def work(self):
        return self.grow()

    def harvest(self):
        if str(self.tomatos) in "[1, 'Red', 2, 'Red', 3, 'Red']":
            self.give_away_all()
            return self.tomatos
        else:
            return 'Error'





p = Gardener('Peter')
print(p.work())
print(p.work())
print(p.harvest())
