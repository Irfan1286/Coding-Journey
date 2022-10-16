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
