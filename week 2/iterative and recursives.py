# this follows concept of factorial

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)     # loop is made as factorial_recursive is used on its own function

number = int(input('Enter Factorial number\n'))
print('Using Iterative method', factorial_iterative(number))   # print used TO give out answer instead of looping and answering
print('using recursive method', factorial_recursive(number))

#Logic
# when number  = 5
# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
# 5 * 4 * 3 * 2 * factorial_recursive(1) Here if number = 1 loop ends