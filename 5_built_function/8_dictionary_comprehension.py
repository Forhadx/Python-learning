
obj = {
    'a': 2,
    'b': 3
}

dic1 = {key: val*2 for key, val in obj.items()}
print(dic1) # {'a': 4, 'b': 6}


dic2 = {key: val*2 for key,val in obj.items() if val%2 != 0}
print(dic2) # {'b': 6}



dic3 = {num:num*2 for num in [1, 2, 3]}
print(dic3) # {1: 2, 2: 4, 3: 6}