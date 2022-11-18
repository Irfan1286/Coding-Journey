#Excercise
#make a program where user needs to input age and the program should say if the person is eligible to drive or not

print('please enter your age!')
age = int(input())

if age > 18:
    print('You are eligible to drive')
elif age == 18:
    print('You are eligible to drive')
else:
    print('You are not eligible to drive')

people = [16, 18, 20, 50, 80, 60 ] #list
if 60 in people:
    print('people of age 60 is not recommended to drive drive')

# in future make it so that I can input in list and also detect age greater than 18 in a list

# people = []
# a = int(input(people))
# print(people)

# Needs loops

#                               Future me

while True:
    ages = input('Enter Numbers only and to quit press [q]')
    if ages.capitalize() == 'Q':
        break
    else:
        try:
            people.append(int(ages))
        except:
            print('Please only input numbers or Q to exit')

Drive_able = [ages for ages in people if ages > 18]

print(Drive_able)