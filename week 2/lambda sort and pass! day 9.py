
def minus(x, y):
    return x-y              # that was a normal function

print(minus(10, 2))

# lambda function is just another way of making a function but it will be one lined only
subtraction = lambda x, y: x-y  #the things after colon will be returned

print(subtraction(20, 2))

z = 20
if z == 20:
    pass
# THe pass function will leave the error (If there is any) and continue with the program! More examples below

def do_something():
    pass
# It also means that, I will come back to it later to solve the function problem

#SORT()
do = [21, 8, 6, 0, 37, 42, 9]
print('before sorting\n', do)
do.sort()               # As the name suggests it sorts in ascending order
print('after sorting\n', do)

z = [['a', 21], ['b', 10], ['c', 45], ['d', 6]]
func = lambda x:x [1]
z.sort(key=func)
print('after adding a function where 1 is returned THe second variable in the list of list')
print('gets sorted as shown as the nth value starts from 0\n', z)
