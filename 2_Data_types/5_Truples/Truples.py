# Truple    - Truple cannot modify

t_1 = (1, 2, 3, 4, 5)

print(t_1)  # (1, 2, 3, 4, 5)

print(t_1[2])   # 3

print(4 in t_1) # True  
print(22 in t_1)  # False


# copy
t_2 = t_1[:]
print(t_2)  # (1, 2, 3, 4, 5)

t_3 = t_1[0 : 3]
print(t_3)  # (1, 2, 3)


# unpacking
x, y, *other, z = (1, 2, 3, 4, 5, 6, 7)

print(x)    # 1
print(y)    # 2
print(other) # [3, 4, 5, 6] 
print(z)    # 7


# length, count, index
t = (4, 2, 1, 4, 2, 6, 8, 2)

# length
print(len(t))   # 8

# count
print(t.count(2))  # 3

# index
print(t.index(8))   # 6
print(t.index(2))   # 1, first 2 index number