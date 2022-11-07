

food = ['chicken', 'sandwich', 'burger', 'pizza', 'candy']

for items in food:
    if items == 'burger':
        print('Your item is found')
        break       # It stops the loop and doesn't go to else statement
    print(items)

else:
    print('This loop ended properly')

