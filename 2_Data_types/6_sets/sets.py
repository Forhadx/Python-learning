""" set   - remove duplicate """
s_1 = {1, 2, 2, 3, 4, 4, 5}

print(s_1)  # {1, 2, 3, 4, 5}

# length
print(len(s_1)) # 5


# copy
new_s = s_1.copy()
print(new_s)    # {1, 2, 3, 4, 5}

# clear
new_s.clear()
print(new_s)    # set()


# ADD 
s_1.add(2)
s_1.add(33)
print(s_1)  # {1, 2, 3, 4, 5, 33}, 2 is already here


# list to set
l = [1, 2, 3, 3, 4, 4, 5]
s = set(l)
print(s)   # {1, 2, 3, 4, 5}

# find
# print(s[0]) , give an error
print(2 in s)   # True


"""
    set methods
        .difference()
        .discard()
        .intersection()
        .union()
        .difference_update()
        .issubset()
        .issuperset()
"""

m = {1, 2, 3, 4, 5}
n = {4, 5, 6, 7}


# .difference()
print(m.difference(n))  # {1, 2, 3}

# .discard()    - REMOVE a value
m.discard(3)    
print(m)    # {1, 2, 4, 5}

# .intersection()
x = m.intersection(n)
print(x) # {4, 5}

x = m & n   # another way
print(x)    # {4, 5}


# .union()
x = m.union(n)
print(x)    # {1, 2, 4, 5, 6, 7}

x  = m | n  # another way
print(x)    # {1, 2, 4, 5, 6, 7}


# .difference_update()  - define difference and remove from set
m.difference_update(n)
print(m)    # {1, 2}



p = {4, 5}
q = {4, 5, 6, 7, 8}

a = {1, 2, 3}
b = {2, 3, 5}

# .issubset()
print(p.issubset(q))    # True
print(q.issubset(p))    # False

print(a.issubset(b))    # False
print(b.issubset(a))    # False


# .issuperset()
print(p.issuperset(q))  # False
print(q.issuperset(p))  # True

