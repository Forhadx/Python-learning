# Parent class, Super class, Base class -> Phone
# Child class, sub class, derived class -> Sumsung, Nokia


class Phone:
    def __init__(self):
        print('You have a phone')
    
    def msg(self):
        print('Message from Phone!')
    

class Sumsung(Phone):
    
    # def __init__(self):
    #     print('You have samsung')
    
    def price(self):
        print('samsung price 12$')

class Nokia(Phone):
    def __init__(self):
        super().__init__()
        print('You have nokia')
    
    def msg(self):      # Method overriding
        super().msg()
        print('Message from Nokia') 
    




s = Sumsung()
s.msg()
s.price()
'''
output:
    You have a phone        -> default parent constructor msg
    Message from Phone!     - msg() from Phone
    samsung price 12$       - price() from  Sumsung
'''

n = Nokia()
n.msg()
'''
output:
    You have a phone    -> call super class and print. without call super class this line not show
    You have nokia      -> Nokia constructor print line

    Message from Phone! -> super msg() call
    Message from Nokia  -> method overridding here
'''




#----------- subclass check method ----------

print(issubclass(Sumsung, Phone)) # True
print(issubclass(Phone, Sumsung)) # False