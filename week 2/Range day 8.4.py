for i in range(10):
    print(i, end = ',')
    print(' to iteration', i + 1, 'after adding' )
print()

for i in range(10, 25):
    print(i, end = ' ')
print()

for i in range(10, 30, 2):          #last argument skips two numbers
    print(i, end = ' ')
print()


for i in range(100, 0, -1):     #Goes backwards 0 means eand at 0 and -1 means go back by 1
    print(i, end = ' ')
print()


total = 0
for i in range(10):                #Addition of total ranges
    total += i+1
print('\n', total)

my_list = list(range(10))       # This bracket cant be in brackets!
print(my_list)