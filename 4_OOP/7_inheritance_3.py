class A:
    def display(self):
        print('A display')

class B():
    def display(self):
        print('B display')


class C(B, A):  # A, B class cannot be subcalss each other
    pass


c  = C()

c.display() # B display -> B class display first