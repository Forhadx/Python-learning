

list1 =[alp for alp in 'hello']
print(list1)    # ['h', 'e', 'l', 'l', 'o']


list2 = [num for num in range(0, 5)]
print(list2)    # [0, 1, 2, 3, 4]


list3 = [num*2  for num in range(0, 5)]
print(list3)    # [0, 2, 4, 6, 8]


arr = [4, 2, 1, 3, 5]
list4 = [num for num in arr if num%2 != 0]
print(list4) # [1, 3, 5]