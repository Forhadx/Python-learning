

set1 ={alp for alp in 'hello'}
print(set1)    # {'e', 'l', 'o', 'h'}   -> duplicate not allow


set2 = {num for num in range(0, 5)}
print(set2)    # {0, 1, 2, 3, 4}


set3 = {num*2  for num in range(0, 5)}
print(set3)    # {0, 2, 4, 6, 8}


arr = [4, 2, 1, 3, 5]
set4 = {num for num in arr if num%2 != 0}
print(set4) # {1, 3, 5}