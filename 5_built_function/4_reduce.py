# import reduce from functools


from functools import reduce

arr = [4, 7, 5, 9]

def sum(s, item):
    print(s,' ', item)
    return s+item

res = reduce(sum, arr, 0)
print(res)  # 25 -> sum of the array


''''
output:
    0   4
    4   7
    11   5
    16   9
    
    25
'''