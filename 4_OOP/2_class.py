# OOP Class structure

class Person:

    def __init__(self, name, age):  # constructor
        self.name = name  # attribute
        self.age = age

    def show(self):  # function
        print('show')


p1 = Person('forhad', 25)

p1.hobby = 'football'

print(p1)  # <__main__.Person object at 0x00000249EAD37CA0> -> physical address

print(p1.name)  # forhad
print(p1.age)   # 25
print(p1.hobby)  # football
# print(p1.salary)  -> salary is not define


'''-------------------------------------------------------
class Person:
    def __init__(self, name):
        self.name = name

    def show(self, name):
        print(f'name is {name}')


p1 = Person('max')

p1.show('forhad') # name is forhad
'''


'''---------------------------------------------------------
class Person:
    def __init__(self, name):
        self.name = name

    def run(self):
        return self


p1 = Person('forhad')

print(p1.run())  # <__main__.Person object at 0x000001CDBB3B2200>

'''
