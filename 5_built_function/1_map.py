

'''------ List -------'''
arr1 = [1, 2, 3]

def double(item):
    return item * 2

result1 = list(map(double, arr1))   # make the result list() otherwise return address
print(result1) # [2, 4, 6]
print(arr1)     # [1, 2, 3]


'''---- String -----'''
str1 = ['sat','bat','cat']

test = list(map(list, str1))
print(test) # [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't']]


