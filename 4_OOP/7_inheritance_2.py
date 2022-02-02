
class Phone:
    def __init__(self, name):
        self.name = name
    
    def msg1(self):
        print('You have a phone')


class Sumsung(Phone):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price

    def show(self):
        print(f'name: {self.name} & price: {self.price}')



s = Sumsung('galaxy', 1200)
s.msg1()    # You have a phone
s.show()    # name: galaxy & price: 1200