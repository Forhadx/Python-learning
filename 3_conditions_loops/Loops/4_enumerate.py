'''
enumerate: is fn which give the index number of
          string , array, truple, dictionary, set
'''


for i, str in enumerate('shamsul'):
    print(i, str)

'''
0 s
1 h
2 a
3 m
4 s
5 u
6 l
'''
print('------------------------------')


arr = [4, 2, 5, 21, 9]
for i, a in enumerate(arr):
    if(a == 5):
        print(f'index of 5 is: {i}')
# index of 5 is: 2

