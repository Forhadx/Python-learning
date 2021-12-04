# OOP

print(type(None))     # <class 'NoneType'>
print(type(True))     # <class 'bool'>
print(type(5))        # <class 'int'>
print(type(5.5))      # <class 'float'>
print(type('bye'))    # <class 'str'>
print(type([]))       # <class 'list'>
print(type(()))       # <class 'tuple'>
print(type({}))       # <class 'dict'>


# --------------------------------------------------
class Car:
    pass


obj = Car()
print(Car)  # <class '__main__.Car'>
print(obj)  # <__main__.Car object at 0x00000195F9737CA0>

print(type(Car))  # <class 'type'>
print(type(obj))  # <class '__main__.Car'>
