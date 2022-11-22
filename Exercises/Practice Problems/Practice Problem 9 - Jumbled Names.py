# Problem Statement:-
# It's result day at school and not everyone is happy.
# You decided to make your friends laugh by jumbling their names to come up with some funny names.
#
# Your program should take the number of names and the names separated by space as input.
# Output should be funny names in the same order.
#
# Input:
# Enter number of friends:
# 3
# Enter the name of your 3 friends:
# Rohan Das
# Shubham Agarwal
# Ritesh Arora
#
# Output:
# Ritesh Das
# Shubham Arora
# Rohan Agarwal

from random import choice
def jumble():
    repeat = int(input("Enter Number Of Friends"))
    print(f"Enter Names Of Your {repeat} Friends:-")
    first_name = []
    last_name = []

    for i in range(repeat):
        names = input()
        # So that error Doesn't come while appending to list
        if ' ' not in names:
            names = names+' '+'.'

        first_name.append(names.split(' ')[0])      # splitting and adding the names to the string!
        last_name.append(names.split(' ')[1])

    for i, first in enumerate(first_name):
        print(f'{first} {choice(last_name)}')       # Choice came from random module


if __name__ == '__main__':
    jumble()