# List

li_1 = [1, 2.3, 'd', True, [2, 5]]
print(li_1) # [1, 2.3, 'd', True, [2, 5]]

li_2 = ['a', 'b', 'c', 'd']
print(li_2[1]) # b
print(li_2[-2]) # c

li_2[1] = 'XX'
print(li_2) # ['a', 'XX', 'c', 'd']



print('---------------- list slicing ----------------')
li_3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(li_3[0: 5: 2])    # ['a', 'c'], [start : end : stepover]


print('---------------- diff list pointing same address ----------------')
li_4 = ['a', 'b', 'c']
a = li_4
a[0] = 'x'
print('li4: ',li_4)  # ['x', 'b', 'c']
print('a: ',a)     # ['x', 'b', 'c']


print('---------------- make copy of list ----------------')
li_5 = ['a', 'b', 'c']
b = li_5[:]
b[0] = 'x'
print('li5: ',li_5)  # ['a', 'b', 'c']
print('b: ',b)     # ['x', 'b', 'c']


print('---------------- another process of copy ----------------')
x = [1, 2, 4]
y = x.copy()
y[0] = 99
print('x: ',x)    # [1, 2, 4]
print('y: ',y)    # [99, 2, 4]