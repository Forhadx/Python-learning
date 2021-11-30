arr = [1,2,3,4,5]

# break
for i in arr:
    if(i == 3):
        break
    print(i) # 1 2
print('------------------------------')

# continue
for i in arr:
    if(i == 3):
        continue
    print(i) # 1 2 4 5
print('------------------------------')

# pass -> didn't do anything. pass all code
for i in arr:
    if(i == 3):
        pass
    print(i) # 1 2 3 4 5


for i in arr:
    # no useful code
    pass # for this pass avoid the error