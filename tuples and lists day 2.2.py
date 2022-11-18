"""
tuples are immutable and comes in () parenthesis
list are mutable and comes in [] brackets
"""
a = 1
prime = [2, 7, 11, 3]  # This is a list
n = prime
n.sort()   # sorts in ascending order
n.reverse()
print(n)

n.append(53)
n.remove(11)
n.insert(2 , 64)   # means adding a new second variable to the list
print(n)

Tup = (9, 3, 6)  # This is a tuple and the variables in it cant change
print(Tup)

#swapping variables
c = 1
b = 3
temp = c
c = b
b = temp
print(c, b)

c,b = b,c   # swaps again
print(c, b)
