
# Iterable - __iter__() or __getitem__()
# Iterator - __next__
# Iteration - while, for etc

def gen(n):
    for i in range(n):
        yield i     # Controls flow of generator

g = gen(3)
print(g)
print(g.__next__())     # due to yeild It takes values only when required and its taken using __next__
print(g.__next__())
print(g.__next__())
try:
    print(g.__next__())
except Exception as error:
    print(error)

name = "Irfan"
ier = name.__iter__()
print(ier)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

num = 48475     # unlike string integers are not iterable
try:
    ier = num.__iter__()
    print(ier)
    print(ier.__next__())
    print(ier.__next__())
    print(ier.__next__())
    print(ier.__next__())
except Exception as j:
    print('\nNot Possible to iterate number you need to use range function')