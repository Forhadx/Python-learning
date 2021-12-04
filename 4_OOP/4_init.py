'''
init -> is a constructor
'''


class Person:
    def __init__(self, name='xx', age=0):
        if(age < 20):
            self.name = name
            self.age = age

    def show(self):
        print(f'name is {self.name} and age is {self.age}')


p1 = Person('forhad', 25)

p1.show()  # if age condition false then show give error

p2 = Person()
p1.show()  # condition false so give error
