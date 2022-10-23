import time

#------------------------MAPPING-------------------------
question = [2, 2, 3, 8, 33, 8, 0, 21, 6]
print(question, 'divide all the numbers by 2')

answer = set(map(lambda x: x/2, question))      # The map function takes in a function and a variable and
                                                # Replaces everything in the function with the variable
print(f'\nThis is the answer = {answer}')
# Essentially map reduces the line of code needed to be written

def square(a):
    return a*a

def cube(a):
    return a*a*a

calculate = [square, cube]

for qus in range(5+1):
    print(f'the square & cube of {qus} is', list(map(lambda x:x(qus), calculate)))
    time.sleep(1.2)
def greater(num):
    return num>5

#------------------------FILTER-------------------------

gr = list(filter(greater, question))        #The map and filter function
print(f'numbers greater than 5 in the list are {gr}')

#------------------------REDUCE-------------------------

# reduce involves reducing a list of items to a single cumulative value
from functools import reduce

total = [1,2,3,4,5]

# num = 0
# for i in total:
#     num += i
# print(num)
#                           INSTEAD of 4 lines this can be done

num = reduce(lambda x,y: x+y, total)
print(num)




