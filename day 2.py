# string slicing
string1 = 'STRING Slicing'
print(string1[4]) # The 4 is written as the string starts from 0,1,2,3,4 making a total of 5 characters!
print(len(string1)) # The len function is used to determine length of a string
print(string1[2:10:3]) # The first number is start second is end of string and third is skip number

string2 = 'negative string slicing'
print(string2[-15:-2]) # 0:-7 means the last seven string will not be counted
#Negative means starting or ending from end

print(string1.isnumeric())  # .isnumeric means checking if the whole string is numbered
print(string1.isalnum())    # .isalnum means checking if the whole string is lettered but its false as there are spaces
print(string1.endswith('Slicing')) # Checks ending term
print(string1.count('i'))   # counts the letters specified in argument
S = string1
print(S.capitalize())   # transforms only first letter to make capital
print(S.lower(), S.upper())
print(S.replace('Slicing', 'replacing'))
print(S.startswith('STRING'))