

a = 6
b = 7
c = 10

x = sum((a,b,c))    #The sum needs a list or touple of numbers in it to add
print(x)            #SUM IS A BUILT-IN FUNTION

def function1(a,b,c,d):
    '''First line of function is a doc string'''
    print('This is function 1', a*b*c*d)

function1(2,2,3,1)  #computer Ignores function lines and when they are called programs return back to them

def math(a,b):
    '''This function will calculate basic maths'''
    print('Division of', a, 'and', b, 'is', a/b)
    print('Multiplication of', a, 'and', b, 'is', a*b)
    print('Addition of', a, 'and', b, 'is', a+b)
    print('Subtraction of', a, 'and',b, 'is', a-b)
    average = (a+b)/2
    return average      #the return is saving the value of average but not as variable

v = math(2,3)      #The return value is being stored in v
print('\n\nAverage value is:',v)
print(math.__doc__)  #It executed the first line only where I described the use of function
math(5, 4)

#--------------------------------------------------------------------------------------------#

print('Enter Num 1')
num1 = input()
print('Enter Num 2')        #ENTER a string to test
num2 = input()

try:
    print('Answer is:', int(num1)+int(num2))
except Exception as e:
    print(e)            # Shows the error area try means if possible else onto next line

print('This is very important piece of code')   # this code will be executed even though if previous/try,except
                                                    # code doesnt work