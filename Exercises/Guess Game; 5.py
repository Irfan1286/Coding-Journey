#write a number where the user needs to guess and only have limited amount of 9 guesses
#the program should tell the amount of guess left and print game over at end
#the program will also tell  higher or lower

num = 38
count = 0
integer = 9
print('guess your numbers','Made by:Irfan')
while (count < 9):
    user = input()
    count = count + 1
    guess = integer - count
    if user == 'close':
        print("You are closing the application.....")
        break
    if int(user) == 3043:
        print('DO YOU WANT TO ENTER SETTINGS?\n Type Y[YES], N[NO]')
        user = input()
        user = user.capitalize()
        if user == 'Y':
            print('\tSETTINGS MENU', '\nA)\tChange the number','\nB)\tChange the number of guesses',
                  '\nC)\tExit Settings Menu')
            chose = input()
            chose = chose.capitalize()
            if chose == 'A':
                print('Enter the value to change')
                value = input()
                num = int(value)
                count = count - 1
                print('Enter and Guess your number')
            elif chose == 'B':
                print('Enter the number of guesses you want to put')
                value = input()
                integer = int(value)
                count = count-1
                print('Enter and Guess your number')
            else:
                count = count - 1
                print('You are out from settings\nGuess and enter your number')
        else:
            count = count - 1
            print('Enter and Guess your Number')
    elif int(user) == num:
        print('\tCONGRATS!!!\nYour guess is correct. You WON with a guess left of: ',guess)
        break
    elif guess == 0 :
        print('Game Over, \n you have 0 GUESSES left')
    elif int(user) < int(num):
        print("The number is higher than ", user, '\nYou have', guess, 'guesses left')
    elif int(user) > num:
        print('The number is lower than', user, '\nYou have', guess, 'guesses left')



