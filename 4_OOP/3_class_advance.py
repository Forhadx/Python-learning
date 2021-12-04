# OOP Class structure

class Person:
    age = 0
    salary = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        Person.salary = salary       # ----- > salary & age get the constructor value

    def show(self):
        print(f'function- name: {self.name}')
        # function- name: forhad
        # print(f'function- name: {Person.name}') # this give an error

        print(f'self age: {self.age} but className age: {Person.age}')
        # self age: 25 but className age: 0

        print(
            f'self salary: {self.salary} but className salary: {Person.salary}')
        # self salary: 1111 but className salary: 1111


p1 = Person('forhad', 25, 1111)

print(f'name: {p1.name}, age: {p1.age}, salary: {p1.salary}')
# OP-> name: forhad, age: 25, salary: 1111

p1.show()

print('---------------------------------------------------------------------')
# help() is use for look full class
help(p1)
'''
Help on Person in module __main__ object:

class Person(builtins.object)
 |  Person(name, age, salary)
 |
 |  Methods defined here:
 |
 |  __init__(self, name, age, salary)
 |      Initialize self.  See help(type(self)) for accurate signature.
-- More  --

'''
