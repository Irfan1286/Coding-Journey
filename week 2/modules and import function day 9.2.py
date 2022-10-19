
import statistics

c = [10, 12, 64, 82, 22, 3, 9, 0, 1, 12]
print('mean =', statistics.mean(c))
print('median =', statistics.median(c))
print('mode =', statistics.mode(c))

import random

print(random.random() * 20)      # This .random again will print numbers 0 to 1 and when multiplied it gives a neew range
print(random.randint(1, 500))    # The arguments are a range in randint and this will print solid integers
print(random.choice(c))          # .choice will random choose elements from a list even strings

#  Exercise- use the two modules to create a program

n = int(input('How many numbers do you want to add to a new list?\n'))
lis = []
for i in range(n):
    z = random.randint(1, 10)
    lis.append(z)
print(lis)

print('DO You Want to Find The', '\n1) MEAN \n2) MEDIAN \n3) MODE \n4) All of the above\t For this set of data')
solution = int(input())
if solution == (1):
    print('mean =', statistics.mean(lis))
if solution == (2):
    print('median =', statistics.median(lis))
if solution == (3):
    print('mode =', statistics.mode(lis))
if solution == (4):
    print('mean =', statistics.mean(lis))
    print('median =', statistics.median(lis))
    print('mode =', statistics.mode(lis))


