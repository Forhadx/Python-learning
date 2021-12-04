'''
    def -> define
'''


# fun-1
def show():
    print('hi')


show()  # hi
# <function show at 0x000002165D712C20>  -> this is address location in memory
print(show)
print('-----------------------------------')


# fun-2 -> pass position arguments
def details(name, age):
    print(f'name is {name} and age is {age}')


details('forhad', 25)  # name is forhad and age is 25
print('-----------------------------------')


# fun-3 -> pass position argument
details(age=30, name='max')  # name is max and age is 30
print('-----------------------------------')


# fun-4 -> keyword arguments
def person(name="Nobody", salary=0):
    print(f"{name}'s salary is {salary}")


person('ratul', 200)               # ratul's salary is 200
person(name='forhad', salary=100)  # forhad's salary is 100
person('max')                      # max's salary is 0
person(20)                         # 20's salary is 0
person()                           # Nobody's salary is 0
