import time     #Just Knew The sleep function
import random

print('The game which you will be playing is snake water game', '\n Where snake drinks water \n gun gets drowned and \n Gun kills snake')

objects = ['Snake', 'Water', 'Gun']
count = 0           #the program will end when count reaches 10
bot_score = 0       # The 2 variables below will track the scores of bot and human
human_score = 0

def choice(a):
    if a == 'S':
        return 'Snake'      # This is for users input to be converted any of the full forms below
    elif a == 'W':
        return 'Water'
    elif a == 'G':
        return 'Gun'

def countdown():
    print('3...')
    time.sleep(1)           #This function will countdown to the results and also update the user on the score
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)
    print(f'You={user} vs BOT={bot}')
    return

# print(choice(input()))
print('Plz Enter One Of The Following', '\n (S) Snake \n (W) Water \n (G) Gun \nDuring the Game')





while (count<10):
    robot = random.randint(0, 2)        # this will randomize computers choice from list 0 to 2 = 3 elemnts total
    bot = objects[robot]                # this will pick the string from list
    print(f'\nround {count + 1}')
    human_choice = input()
    human = human_choice.capitalize()
    user = choice(human)
    time.sleep(1)

    if user == bot:
        countdown()
        print('Draw')

    elif bot == 'Snake' and user == 'Water':
        bot_score += 1
        countdown()
        print(f'Defeat {human_score}:{bot_score}')
    elif bot == 'Water' and user == 'Gun':
        bot_score += 1
        countdown()
        print(f'Defeat {human_score}:{bot_score}')
    elif bot == 'Gun' and user == 'Snake':
        bot_score += 1
        countdown()
        print(f'Defeat {human_score}:{bot_score}')

    elif bot == 'Snake' and user == 'Gun':
        human_score += 1
        countdown()
        print(f'Victory!!{human_score}:{bot_score}')
    elif bot == 'Gun' and user == 'Water':
        human_score += 1
        countdown()
        print(f'Victory!! {human_score}:{bot_score}')
    elif bot == 'Water' and user == 'Snake':
        human_score += 1
        countdown()
        print(f'Victory!!{human_score}:{bot_score}')
    else:
        print('Enter a valid input')
    count += 1
    while count == 10:
        if human_score > bot_score:
            print(f'\tYou Win With a score of {human_score}:{bot_score}')
        elif bot_score > human_score:
            print(f'\tYou Lost With a score of {human_score}:{bot_score}')
        else:
            print("The match was a draw")
        print('Do you want to play Again? Y[YES], N[NO]')
        play = input()
        if play.capitalize() == 'Y':
            count = 0
        else:
            print('closing the application...')
            time.sleep(3)
            break
