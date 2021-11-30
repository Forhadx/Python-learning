'''
    help
    __doc__
'''



def test(a):
    '''
    note: this is dangers line.
    '''
    print(a)

test(10) # 10

# test() # give an error

# process-1
help(test) # this process, can get all comments and function name with parameter
'''
test(a)
    note: this is dangers line.
'''

# process-2
print(test.__doc__) # this is another process to get all comments only
'''
note: this is dangers line.
'''