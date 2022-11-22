# Problem Statement:-
# Rohan das is a fraud by nature.
# Rohan Das wrote a python function to print a multiplication table of a given number and
# put one of the values (randomly generated) as wrong.
#  Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!
#
# So you decided to use your python skills to counter Rohan’s actions by writing a python program that
# validates Rohan’s multiplication table.
# Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
#
# Note: Rohan’s function returns a list of numbers like this
#
# Rohan Das’s Function Input:
# rohanMultiplication(6)
#
# Rohan’s function returns this output:
# [6, 12, 18, 26, …., 60]
#
# You have to write a function isCorrect(table, number) and
# return the index where rohan’s function is wrong and print it to the screen!
# If the table is correct, your function returns None

'''
author -  Mohammed Irfan
date - 22 September 2022
purpose - Practice and Fun
'''

def WrongMultiplication(number):
    table = []
    for i in range(10):
        table.append(number*(i+1))

    # Random Numbers:-
    from random import randint
    randlist = randint(1,9)    # Takes a random number for index of list to change
    randnum = (table[randlist])-1     # Changes the number according to the index

    # Table Modification To Make it wrong:-
    table.pop(randlist)         # deletes that index
    table.insert(randlist, randnum)     # replaces the index with wrong number

    return table

def isCorrect(table, number):

    correct_table = []
    for i in range(10):
        correct_table.append((i+1)*number)

    if correct_table != table:
        return '\nThere is mistake in table provided by the maker'
    else:
        return None

if __name__ == '__main__':
    try:
        number = int(input('Enter The Number For Which You Want The Table:-\t'))
    except:
        print('Please Enter a valid input next time')
        exit()
    print(WrongMultiplication(number))      # Prints Wrong Multiplication table
    print(isCorrect(WrongMultiplication(number), number))   # Tells user if the table is wrong
