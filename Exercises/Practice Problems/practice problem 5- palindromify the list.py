# Problem Statement:-
# You are given a list that contains some numbers.
# You have to print a list of the next palindromes only if the number is greater than 10;
# otherwise, you will print that original number.
#
# Input:
# [1, 6, 87, 43]
#
# Output:
# [1, 6, 88, 44]

'''
author - Mohammed Irfan
date - 20 september 2022
purpose - Practice of python programming from code_with_Harry
'''

palindrome_list = input('Please enter your numbers with "," in between :- \t')

try:
    list1 = list(map(int, palindrome_list.split(',')))  # MAPS int type to the variable in split list
except:
    print('Please enter a valid input and make sure there is no "," at the end')
    exit()
result = []
for num in list1:
    while True:         # this loop checks for the next palindrome by keeping on adding numbers until it is a palindrome
        num += 1
        if num < 10:
            result.append(num-1)
            break           # if number is less than 10 it will be added to the list

        elif str(num) == str(num)[::-1] and num>10:
            result.append(num)
            break


print(f'Your Input was :- {list1} \n& next palindromes in the list greater than 10 are :- {result}')




