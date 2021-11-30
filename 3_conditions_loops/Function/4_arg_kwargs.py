'''
*args 
**kwargs

-> name can be anything but args, kwargs are developer choice
'''

# For position agruments
def summation(*args):
    print(*args) # 1 2 3 4 5
    print(args)  # (1, 2, 3, 4, 5) return truples

    for i in args:
        print(i) # 1 2 3 4 5
    
   # for i in *args: -> give an error

summation(1,2,3,4,5)
print('----------------------------')


# For keyword arguments
def show(**kwargs):
    # print(**kwargs) -> give an error
    print(kwargs) # {'a': 'aa', 'b': 'bb'} -> dictionary value

    for i in kwargs.values():
        print(i) # aa bb

show(a='aa', b='bb')