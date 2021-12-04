'''
private
    - There is no private declaretion in py
    - use ( _ ) before variable to identify the private value
'''


class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def show(self):
        # print(f'name:- {self.name}')  #-> this line can not access
        print(f'age:- {self.age}')
        pass


p1 = Person('forhad', 25)

p1.show()
