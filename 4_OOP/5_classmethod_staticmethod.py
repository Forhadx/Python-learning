'''
@classmethod
@staticmethod
'''


class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'name is {self.name}')

    @classmethod
    def show1(cls, n):
        print(n)  # -> forhad
        return cls(n)  # cls = Person, n value pass to constructor

    @staticmethod
    def show2(m):
        print(m)


Person.show1('forhad')  # -> clssmethod

Person.show2('max')  # -> staticmethod
