
#Things i learned 01
#this is comment
'''
this
is
multi line comment can be differnt color every time
'''
print('This letter n after \ will  make a new line example \nlike this')
print('this letter t after \ will act like tab example \tlike this')
print('The end command will merge the next line with it', end='')
print('but it needs to be done after a comma on print statement')

#Excercise simple calculator
print('Enter your first number to ADD')
Var1 = input()
print('Enter your second number to ADD')
Var2 = input()

#Var1 and Var2 is String as variables are string data by default
print('Your number is ...\n', int(Var1) + int(Var2))
#The upper statement changed Var1 and Var2 a.k.a string, which is converted to integer


Var3 = 'this is string which is classified as str()'
Var4 = 34.23   #this is a float classified as float()

print(type(Var3),type(Var4))
