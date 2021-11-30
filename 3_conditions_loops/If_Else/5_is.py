"""
(==) is only check the boolean value
(is) is check the reference value
"""


print(1 == True) # True

print('' == 1) # False
print('1' == 1) # False
print('ss' == 1) # False

print(10 == 10.0) # True

print([] == 1) # False
print([] == []) # True
print([1,2,3] == [1,2,3]) # True
 
print('-----------------------------')

print(1 is True) # False

print('' is 1) # False
print('1' is 1) # False
print('ss' is 1) # False

print(10 is 10.0) # False

print([] is 1) # False
print([] is []) # True
print([1,2,3] is [1,2,3]) # False


print('---------------------------------')

print(1 is 1) # True

a = 1
b = a
print(a is b) # True

x = [1,2,3]
y = x
print(x is y) # True