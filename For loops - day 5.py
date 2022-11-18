# Make a list and print only integers greater than 6

list1 = [3, 8, 125, 4, 'hfjf']

for item in list1:
    if str(item).isnumeric() and item > 6:                  # .Isnumeric is used for string data type
        print(item)                                         #   so it needs to be converted to string
      # END OF EXCERCISE
      # NOTE
      # for loop will run until content of list dict or anything isnt finished

print("\n\tNEXT")

list2 = [['larry', ['BEST', 20]] , ['Harry', 3], ['Carry', 8]]        #to make a dict from list names need to be defined
dict1 = dict(list2)

"""for items in dict1:
    print(items)"""

for items,jumps in dict1.items():             # .items is used to define that there are more values to print'''
    print(items,'his jump is:\n', jumps)                        # for can assign values to the variable, and in will be location