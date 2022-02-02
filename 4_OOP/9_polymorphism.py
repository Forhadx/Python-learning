# Polymorpish -> single method have different role

class Car:
    def display(self):
        print('This is a car')


class Bus:
    def display(self):
        print('This is a bus')


c = Car()
c.display() # This is a car

b = Bus()
b.display() # This is a bus



# method name differe but use in differet way