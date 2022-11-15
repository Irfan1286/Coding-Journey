
# raise is used to stop the program if some conditions are not met such as incorrect input

name = input('Enter Your name:\n')

if name.isnumeric():
    raise Exception('You Have to enter a valid string')         # Normal exception = General Exception

salary = input('Enter The Amount of Money You Earn:\n')

if salary.isalpha():
    raise Exception('Sorry this is invalid')

permission = input()

if permission != '1':
    raise PermissionError('You have to input the correct pin to access the rest of the program')

print(f'So your name is {name} and your salary = {salary}_dollars!')

entry = input('Enter Username:\n').capitalize()
try:
    print(a)        # A is not defined so the program will go to Exception

except Exception as e:
    if entry == 'Harry':
        raise Exception('Sorry but you are blocked!')

    print('Variable a is not defined and the Exception has been executed successfully')

# For more Exceptions Type: built in exceptions python

# BTW 'is' is used for returning true for same object
# But '==' is used to return true for same values

a = [2, 4, 6, 8]
b = [2, 4, 6, 8]
print(a is b)       # both are different objects that have different memory location so it will return false
