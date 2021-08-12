"""
    - string
    - Escape Sequence
    - string concatenation
    - type conversation
    - formatted String
    - 
"""


""""----------------- string ------------------"""

print('hi') # hi

print("hello") # hello


""""----------------- Escape Sequence -------------"""

print("i'm cool") # i'm cool

print('i\'m cool') # i'm cool

print("It\'s \"kind of\" sunny") # It's "kind of" sunny


""""----------------- string concatenation ----------------"""

"""
    print('hi ' + 4) # error
    print('hi ' - 4) # error
    print('hi ' / 4) # error
"""

print('hi ' * 4) # hi hi hi hi

print('+' * 5) # +++++


""""---------------- type conversation ----------------"""

# string to int and float 
a = '21'
print(int(a)) # 21 , int value

print(float(a)) # 21.0 , float value


# int and float to string
b = 11
print(str(b)) # 11 , str value

c = 22.21
print(str(c)) # 22.21 , str value


""""---------------- formatted String ----------------"""

name = 'forhad'
age = 24

print(f'my name is {name}. i am {age}') 
# my name is forhad. i am 24

print('my name is {}'.format('forhad'))
# my name is forhad

print('I am {}'.format(age))
# I am 24


""""---------------- String Indexes ----------------"""

num = '01234567'

print(num[2]) # 2

print(num[-1])  # 7
print(num[-3])  # 5


#[start:stop]
print(num[1:3]) # 12
print(num[2:6]) # 2345

#[start:stop:stepOver]  // avoid stepover values
print(num[0:5:2]) # 024
print(num[0:7:3]) # 036


print(num[0:0]) # no value print

print(num[2: ]) # 234567
print(num[ :5]) # 01234

print(num[ : : 2]) # 01234567 , cz start,end is not define so print all val
print(num[::-1])    # 76543210, reverse value print
print(num[::-2])    # 7531, reverse value with stepover



""""---------------- String built in function ----------------"""

name = 'shAmSuL HaqUE foRhAd'

# length of string
print(len(name))    # 6

# uppercase
print(name.upper()) # SHAMSUL HAQUE FORHAD

# lowercase
print(name.lower()) # shamsul haque forhad

# capitalize
print(name.capitalize()) # Shamsul haque forhad

# find
print(name.find('HaqUE')) # start from index 8

# replace(old, new)
print(name.replace('HaqUE', 'haq')) # shAmSuL haq foRhAd

