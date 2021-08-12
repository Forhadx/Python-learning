# List

li_1 = [1, 2.3, 'd', True, [2, 5]]
print(li_1) # [1, 2.3, 'd', True, [2, 5]]

li_2 = ['a', 'b', 'c', 'd']

print(li_2[1]) # b
print(li_2[-2]) # c

li_2[1] = 'XX'
print(li_2) # ['a', 'XX', 'c', 'd']


# list slicing
li_3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(li_2[0: 5: 2])    # ['a', 'c'], [start : end : stepover]



# diff list pointing same address
li_4 = ['a', 'b', 'c']
a = li_4
a[0] = 'x'
print(li_4)  # ['x', 'b', 'c']
print(a)     # ['x', 'b', 'c']


# make copy of list
li_5 = ['a', 'b', 'c']
b = li_5[:]
b[0] = 'x'
print(li_5)  # ['a', 'b', 'c']
print(b)     # ['x', 'b', 'c']