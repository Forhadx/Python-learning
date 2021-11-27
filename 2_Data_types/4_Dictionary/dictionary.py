""" Dictionary"""

print('----------------- initial dictionary ---------------')
d_1 = {
    'a': [11, 22, 33],
    'b': 'hello',
    'c': True
}

print(d_1)          # {'a': [1, 2, 3], 'b': 'hello', 'c': True}
print(d_1['a'])     # [1, 2, 3]
print(d_1['a'][2])  # 33


print('------------------ copy dictionary -------------------')
x = d_1.copy()
print(x)  # {'a': [11, 22, 33], 'b': 'hello', 'c': True}


print('------------------ Dicionary in List -------------------')
l_1 = [
    {
        'a': [1, 2, 3],
        'b': 'hi'
    },
    {
        'a': [5, 6, 7],
        'b': 'hello'
    }
]

print(l_1)  # [{'a': [1, 2, 3], 'b': 'hi'}, {'a': [5, 6, 7], 'b': 'hello'}]
print(l_1[1]['a'][1])   # 6



print('------------------ Dictionary keys -------------------')
d_2 = {
    'aa' : 'hi',
    12: [1, 3, 5],
    True: 'bro'
    # [22] : 'hello'    , array not support
}

print(d_2[12][1])  # 3
print(d_2[True])   # bro




print('------------------ Dictionary Methods -------------------')
user = {
    'name': 'rose',
    'age': 23
}

# print(user['a'])  , 'a' isn't exist its give error

print(user.get('name')) # rose

print(user.get('name', 'jack')) # rose, if 'name' isn't exist then jack displayed

print(user.get('a'))    # None , 'a' isn't exist but return None

print(user.get('a', 21))  # 'a' is not exist , but give the value 21 of 'a'

print(user) # {'name': 'rose', 'age': 23}, 'a' value dnt add in user dict



print('------------------ Check Dictionary -------------------')
u = {
    'a': 'aaa',
    'b': 'bbb',
    'c': 'ccc'
}

# its check keys
print('a' in u)    # True
print('x' in u)    # False

# check keys 
print('a' in u.keys())  # True
print('y' in u.keys())  # False

# check values 
print('aaa' in u.values())  # True
print('xxx' in u.values())  # False

# Items
print(u.items())    # dict_items([('a', 'aaa'), ('b', 'bbb'), ('c', 'ccc')])  



print('------------------ add, remove (val, keys) in Dictionary -------------------')
u_1 = {
    'a': [1, 2, 3],
    'b': 'hello',
    'c': 'c'
}

# remove a key
print(u_1.pop('a')) # [1, 2, 3]
print(u_1)  # {'b': 'hello', 'c': 'c'}


# add new keys and values
u_1.update({'x':'xxx'})
print(u_1)  # {'b': 'hello', 'c': 'c', 'x': 'xxx'}

print('---------------- clear ------------------')
#  clear dictionary
print(u_1.clear())  # None
print(u_1)  # {}



