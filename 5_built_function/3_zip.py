
'''------- zip() -------'''

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = [4, 5, 6, 88]
touple1 = (7, 8, 9)


res1 = list(zip(arr1, arr2))
print(res1)     # [(1, 4), (2, 5), (3, 6)]


res2 = list(zip(arr1, arr3))
print(res2) # [(1, 4), (2, 5), (3, 6)]


res3 = list(zip(arr1, touple1))
print(res3) # [(1, 7), (2, 8), (3, 9)]


res4 = list(zip(arr1, arr2, arr3))
print(res4) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]