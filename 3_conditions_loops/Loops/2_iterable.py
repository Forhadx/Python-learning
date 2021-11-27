# iterate -> one by one check each item

# dictionary iterable
user = {
    'name': 'forhad',
    'age': 25,
    'hobby': 'football'
}

#------- only key shows
for item in user:
    print(item)
'''
name
age
hobby
'''
print('--------------------')

#----- both key, items ------
for item in user.items():
    print(item)
'''
('name', 'forhad')
('age', 25)
('hobby', 'football')
'''
print('--------------------')

#----- both key, items in different ways------
for k, v in user.items():
    # k , v = item
    print(k,  v)
'''
name forhad
age 25
hobby football
'''
print('--------------------')


#------- dic values ---------
for item in user.values():
    print(item)
'''
forhad
25
football
'''
print('--------------------')

#------- dic keys ---------
for item in user.keys():
    print(item)
'''
name
age
hobby
'''