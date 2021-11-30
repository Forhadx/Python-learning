'''
    Find the duplicate from the array
'''
arr = ['a','a','b','c','c','d']

dupliate = []

for val in arr:
    if arr.count(val) > 1:
        if val not in dupliate:
            dupliate.append(val)

print(dupliate)  # ['a', 'c']