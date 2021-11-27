
'''
range(val)
range(start, end)
range(start, end, step)
range(end, start, -step)  -> reverse
'''

# VLAUE
for i in range(5):
    print(i) # 0 1 2 3 4
print('----------------------')

# START TO END
for i in range(0, 5):
    print(i) #  0 1 2 3 4
print('----------------------')

# start to end with stepover
for i in range(0, 10, 2):
    print(i) # 0 2 4 6 8
print('----------------------')

# reverse
for i in range(5, 0):
    print('r: ',i) # this is not going to work
print('----------------------')

# reverse with stepover
for i in range(5, 0, -1):
    print(i) # 5 4 3 2 1


# make list
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(3, 8))) # [3, 4, 5, 6, 7]
print(list(range(2, 10, 2))) # [2, 4, 6, 8]
print(list(range(12, 3, -2))) # [12, 10, 8, 6, 4]