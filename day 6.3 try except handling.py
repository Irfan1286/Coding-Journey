
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