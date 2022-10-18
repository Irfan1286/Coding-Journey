
names = ['Harry', 'Rohan', 'Hammad']
loop = 0


def health():
    print('What Do You Want To Access'
        , '\nA)\tDiet', '\nB)\tExercise')           # This function is given so that not needed to write
    return                                          # Multiple times


def getdate():
    import datetime                             # This function gives date and time
    return datetime.datetime.now()


def change(a, food_ex):
    time = str(getdate())                       # This function edits the required files
    a.write('[')                                # and A is the file name to edit into!
    a.write(time)                               # food_ex means food or exercise values taken from user
    a.write(']\t')
    a.write(food_ex)
    a.write('\n')
    return

def ate_ex(b, c):
    with open(b, 'a') as a:                         # IN This function b is the file name(including the format.txt)
        print('What did you', c, 'today?')          # and in 'c' the value of eat or exercise is shown
        change(a, input())
        print('Edit is done successfully')

while (loop == 0):
    mode = input('Do you want to LOG or RETRIEVE data from client files?\n')
    choice = mode.upper()           # This is either Edit or Read File mode

    if choice == 'LOG':
        print('Enter\n1)\tHarry\n2)\tRohan\n3)\tHammad')
        client = int(input())           # The list of names is given on top as variable names
        client -= 1                     # -1 as list starts from 0,1,2 (its irritating)
        edit = names[client]            # takes the name from list according to client value
        print(edit.upper())
        if edit == 'HARRY':
            health()
            access = input()
            if access.capitalize() == 'A':
                ate_ex('Harry diet.txt', 'eat')
            if access.capitalize() == 'B':
                ate_ex('Harry Exercise.txt', 'perform')

        elif edit == 'ROHAN':
            health()
            access = input()
            if access.capitalize() == 'A':
                ate_ex('Rohan diet.txt', 'eat')
            elif access.capitalize() == 'B':
                ate_ex('Rohan Exercise.txt', 'perform')

        elif edit == 'Hammad':
            health()
            access = input()
            if access.capitalize() == 'A':
                ate_ex('Hammad diet.txt', 'eat')
            elif access.capitalize() == 'B':
                ate_ex('Hammad Exercise.txt', 'perform')

    elif choice == 'RETRIEVE':
        print('Enter the name of client to retrieve data from!\n1)\tHarry\n2)\tRohan\n3)\tHammad')
        client = int(input())
        client -= 1
        edit = names[client]
        print(edit.capitalize())

        if edit == 'Harry':
            print('Which data do you want to retrieve from,', '\n1)DIET \n\tOR \n2)EXERCISE')
            retrieve = int(input())
            if retrieve == (1):
                with open('Harry diet.txt') as g:
                    a = g.read()
                    g.seek(0)
                    print(a)
            elif retrieve == (2):
                with open('Harry Exercise.txt') as g:
                    a = g.read()
                    g.seek(0)
                    print(a)
            else:
                print('Please Enter Option 1 or 2 Only')

        elif edit == 'Rohan':
            print('Which data do you want to retrieve from,', '\n1)DIET \n\tOR \n2)EXERCISE')
            retrieve = int(input())
            if retrieve == (1):
                with open('Rohan diet.txt') as g:
                    a = g.read()
                    g.seek(0)
                    print(a)
            elif retrieve == (2):
                with open('Rohan Exercise.txt') as g:
                    a = g.read()
                    g.seek(0)
                    print(a)
            else:
                print('Please Enter Option 1 or 2 Only')
        elif edit == 'Hammad':
            print('Which data do you want to retrieve from,', '\n1)DIET \n\tOR \n2)EXERCISE')
            retrieve = int(input())
            if retrieve == (1):
                with open('Hammad diet.txt') as g:
                    a = g.read()
                    g.seek(0)
                    print(a)
            elif retrieve == (2):
                with open('Hammad Exercise.txt') as g:
                    a = g.read()
                    g.seek(0)
                    print(a)
            else:
                print('Please Enter Option 1 or 2 Only')
        else:
            print('Please Choose A Valid Option')

    print('Do you want to use this program again?', '\n\tY[YES]\tN[NO]')
    iterate = input()
    if iterate.upper() == 'N':
        loop = 1
