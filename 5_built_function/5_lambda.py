
from functools import reduce

arr = [3, 4, 5, 6]

res1 = list(map(lambda item: item*2 , arr))
print(res1) # [6, 8, 10, 12]


res2 = list(filter(lambda item: item%2 != 0, arr))
print(res2) # [3, 5]


res3 = reduce(lambda acc, item: acc+ item, arr, 0)
print(res3) # 18