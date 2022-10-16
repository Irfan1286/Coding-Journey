
num = int(input('plz enter your Number\n'))
star = '*'
boolean = int(input('Enter 1 OR 0\n'))
if boolean == 1:
    count = 0
    while (num>count):
        count += 1
        pattern = count
        print(pattern*star)

if boolean == 0:
    count = -1
    while (num>count):
        count += 1
        pattern = num - count
        print(pattern*star)
        if pattern == 1:
            break

# elif boolean == 0:
#     print(num*star)