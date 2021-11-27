"""
    length: len(arr)

    add: arr.append(val)
    add by index: arr.inset(index, val)
    marge list: arr1.extend(arr2)

    remove: arr.pop()
    remove by index: arr.pop(index)
    clear list: arr.clear()

    find index: arr.index(val)
    bool check: print(val in arr)  // t / f
    count: arr.count(val)

    sort: arr.sort()
    sorted copy: sorted(arr)  // arr not sorted 

    reverse: arr.reverse()
    reverse copy: arr[::-1]

    rage: list(range(10)), list(range(3, 20))

    join: ' '.joint(arr)

    list unpacking: a, b, *c = [1, 2, 3, 4, 5, 6]

"""




print('-----------list Length ---------------')
# list length
#from typing import List
l = [1, 2, 3, 4]
print(len(l)) # 4


print('-----------list Add ---------------')
# Adding value in last index
m = ['a', 'b', 'c']
m.append('d')
print(m)    # ['a', 'b', 'c', 'd']

# Adding value by index: list.insert(index, value)
n = ['a', 'b', 'c', 'd']
n.insert(1, 'X')
print(n)    # ['a', 'X', 'b', 'c', 'd']

# merge two list
li_1 = [1, 2, 3]
li_2 = ['a', 'b']
li_1.extend(li_2)
print(li_1) # [1, 2, 3, 'a', 'b']


print('-----------list Remove ---------------')
# remove last index val
a = [1,2,3,4,5]
a.pop()
print(a)    # [1, 2, 3, 4]

# remove value by index number
b = [1, 2, 3, 4, 5]
b.pop(3)
print(b)    # [1, 2, 3, 5]


# clear a list all values
c = [1, 2 , 3]
c.clear()
print(c)    # []



print('----------- find index , Count value  --------------')
d = ['a', 'b', 'c', 'd', 'e']
print(d.index('c')) # 2

# check value is in list
print('b' in d) # True
print('x' in d) # False

# use in string
print('i' in 'he is in home')   # True


# count value in list 
e = ['a', 'b', 'a', 'c', 'a']
print(e.count('a')) # 3


print('----------- list sorting ---------------')
# sort
f = [3, 5, 2, 1, 6, 2]
f.sort()
print(f)    # [1, 2, 2, 3, 5, 6]

# sorted - produce a new array
arr = [3, 2, 5, 9, 2, 4]
arr2 = sorted(arr)
print('arr: ',arr)     # [3, 2, 5, 9, 2, 4]
print('arr2: ',arr2)   # [2, 2, 3, 4, 5, 9]


print('----------- reverse ---------------')
# reverse list
r = [41, 27, 10, 30]
r.reverse()
print('reverse: ',r)    # [30, 10, 27, 41]

# copy a list and reverse
p = [1, 2, 3, 4]
q = p[::-1]
print('q: ',q)  # [4, 3, 2, 1]
print('p: ',p)    # [1, 2, 3, 4]



print('----------- range ---------------')
print(list(range(4, 10)))  # [4, 5, 6, 7, 8, 9]
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


"""----------- join ---------------"""
m = ['my', 'name', 'is', 'zozo']

middle = '!'
n_1 = middle.join(m)
print(n_1)    # my!name!is!zozo

n_2 = ' '.join(m)
print(n_2)  # my name is zozo


"""----------- list unpacking ---------------"""

a,b,c = [10, 20, 30]
print(a)    # 10
print(b)    # 20
print(c)    # 30

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)    # 1
print(b)    # 2
print(c)    # 3
print(other)# [4, 5, 6, 7, 8]
print(d)    # 9