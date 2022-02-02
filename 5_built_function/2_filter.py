
arr = [3, 2, 5, 1, 4]

def check_odd(item):
    return item % 2 != 0


res = list(filter(check_odd, arr))

print(res)   # [3, 5, 1]