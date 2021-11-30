# -----while loop --------
i = 0
while i < 5:
    print(i)  # 0 1 2 3 4
    i += 1
print('----------------------------------')


# ----------- break in while loop ----------
'''
i = 0
while 0 < 5:
    print(i) # 0 0 0 0 0 ...... 

-> here print go to inifinite loop
-> so use break, its give one value not infinite
'''

i = 0
while 0 < 5:
    print(i) # 0
    break
print('------------------------------------')


#--------- while else ----------------

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print('done!')
'''
0 1 2 3 4 
done!

-> while true or false no matter else cluse will be print here
'''
print('---------------------------------------')

i = 0
while i < 5:
    print(i)
    i += 1
    break
else:
    print('done!')
'''
0

-> if there is break than else not work
'''
print('----------------------------------------')


#----------- use of while loop for array ---------
arr = [10, 20, 30, 40, 50]
i = 0
while i < len(arr):
    print(arr[i])
    i +=1
# 10 20 30 40 50
print('------------------------------------------')


#------------ infinite, limited - input take ------------

# while True:
#     input('enter your name ')

while True:
    name = input('enter name: ')
    if(name == 'f'):
        break
# when get 'f' then loop will be finish
