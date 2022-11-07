
'''
ls = []
for i in range(50):
    if i%3 == 0:
        ls.append(i)
print(ls)
# This can be written in a single line by the method of list comprehensions
'''

# ------------------LIST COMPREHENSIONS------------------

ls = [i for i in range(5)]
print(ls)

Secondlist = [i for i in range(30) if i%3 == 0]     # First i second for loop third condition
print(Secondlist)

# ------------------DICTIONARY COMPREHENSIONS------------------

dict1 = {i:f'value = {i}' for i in range(10) if i%2 == 0}  #Makes a list with the given commands in a line
print(dict1)

dict1 = {value:key for key,value in dict1.items()}      # changes positions in the dictionary
print(dict1)


# ------------------SET COMPREHENSIONS------------------

dresses = {dress for dress in ['dress a','dress b','dress a','dress b']}  # AS usual sets cant repeat same things
print(dresses)

# ------------------GENERATOR COMPREHENSIONS------------------
odd_num = (i for i in range(20) if i%2 != 0)
print(odd_num)
print(odd_num.__next__())
print(odd_num.__next__())
print(odd_num.__next__())
print(odd_num.__next__())
print(type(odd_num))

# Summary to use this method you need to assign the item to the type class and then write for loop and
# then write conditions if needed and with just a gap no comma or anything needed to do so

"""
take a list as input from user 
and ask the user which type of comprehension to make except for generator comprehension
then make the comprehension and print it
"""

user_input = list(input('Make your list').split(' '))
comprehension = input('Enter type of comprehension').capitalize()

if comprehension == 'Set':
    new = {i for i in user_input if int(i)%5 == 0}
    print(new)
elif comprehension == 'List':
    lg = [i for i in user_input if int(i) % 5 == 0]
    print(lg)
elif comprehension == 'Dictionary':
    hf = {i:f'The number {i} can be divisible by 5' for i in user_input if int(i) % 5 == 0}
    print(hf)