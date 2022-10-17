# fibonchee sequence adds up two numbers where one is previous and other is previouses previous

print('Enter the the limit for fibonache sequence')
num = int(input())

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        seq = fibonacci(n-1)+fibonacci(n-2)     #Seq means sequence
        print(seq)                              # Recursive is used best for mathematical problems but harder to tracback and find problems while debugging
        return seq

print(fibonacci(num))


# The usage of same function in the function is recursion