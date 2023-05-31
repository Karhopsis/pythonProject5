class Name():

    def __init__(self,name):
        self.name = name
        print('Your name is: ', name)

    def set_name(self,n):
        self.name = n

    def get_name(self):
        return self.name



p = Name('Viktor')
p.set_name('Vasil')