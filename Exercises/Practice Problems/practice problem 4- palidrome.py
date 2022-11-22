# Problem Statement:-
# A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
# 676, 616, mom, 100001.
#
# You have to take a number as an input from the user.
# You have to find the next palindrome corresponding to that number.
# Your first input should be the number of test cases and then take all the cases as input from the user.
#
# Input:
# 3
# 451
# 10
# 2133
#
# Output:
# Next palindrome for 451 is 454
# Next palindrome for 10 is 11
# Next palindrome for 2311 is 2222
'''
author - Mohammed Irfan
date - 20 september 2022
purpose:- practice from code with harry!

'''



repeat = ''
while type(repeat) != int:
    try:
        repeat = int(input('How many numbers do you want to enter:- '))
    except:
        print('Enter A Valid Value')

for i in range(repeat):
    palindrome = ''
    while type(palindrome) != int:
        try:
            palindrome = int(input('Enter Your Value:- '))
        except:
            print("Please Enter A Valid Number")

    while True:             # keeps on adding until the palindrome for the number is same
        palindrome += 1
        if palindrome == int(str(palindrome)[::-1]):
            print(f'this is the next palindrome {palindrome}')
            break












