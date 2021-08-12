# list length
l = [1, 2, 3, 4]
print(len(l)) # 4


"""-----------list Add ---------------"""
# Adding value in last index
m = ['a', 'b', 'c']
m.append('d')
print(m)    # ['a', 'b', 'c', 'd']


# Adding value by index: list.insert(index, value)
n = ['a', 'b', 'c', 'd']
n.insert(1, 'X')
print(n)    # ['a', 'X', 'b', 'c', 'd']


# merge two list
li_1 = [1, 2, 3]
li_2 = ['a', 'b']
li_1.extend(li_2)

print(li_1) # [1, 2, 3, 'a', 'b']


"""-----------list Remove ---------------"""
# remove last index val
a = [1,2,3,4,5]
a.pop()
print(a)    # [1, 2, 3, 4]

# remove value by index number
b = [1, 2, 3, 4, 5]
b.pop(3)
print(b)    # [1, 2, 3, 5]


# clear a list all values
c = [1, 2 , 3]
c.clear()
print(c)    # []