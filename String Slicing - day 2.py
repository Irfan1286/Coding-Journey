# string slicing
string1 = 'STRING Slicing'

print(string1[4])   # The 4 is written as the string starts from 0,1,2,3,4 making a total of 5 characters!
# Prints N from string

print(len(string1))
# Prints length of string

print(string1[2:10:3])
# starts from length 2 and ends on 10 and skips 3 letters to print R, G, and L


# Negative means starting or ending from end
string2 = 'negative string slicing'
print(string2[-15:-2])
# will start counting from end and stop at counting of 2 coming from end

print(string2[0:-7])
# 0:-7 means the last seven string will not be counted


'''//////////////////////////Boolean checks/////////////////////////'''
print(string1.isnumeric())
# .isnumeric means checking if the whole string is numbered

print(string1.isalnum())
# returns true only if the string contains letters not even gaps

print(string1.endswith('Slicing'))
# returns true if ending term matches

print(string1.count('i'))
# counts the letters repeated, specified from the argument from in the given string


S = string1
print(S.capitalize())   # transforms only first letter to make capital
print(S.lower(), S.upper())
print(S.replace('Slicing', 'replacing'))
print(S.startswith('STRING'))