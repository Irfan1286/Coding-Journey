# Generate a random integer from a to b.
# You and your friend have to guess a number between two numbers, a and b.
# a and b are inputs taken from the user. Your friend is player 1 and plays first.
# He will have to keep choosing the number, and your program must tell
# whether the number is greater than the actual number or less than the actual number.
# Log the number of trials it took your friend to arrive at the number.
# You play the same game, and then the person with the minimum number of trials wins!
# Randomly generate a number after taking a and b as input and don’t show that to the user.
#
# Input:
# Enter the value of a
# 4
# Enter the value of b
# 13
#
# Output:
# Player1:
#
# Please guess the number between 4 and 13
#
# 5
#
# Wrong guess a greater number again
# 8
# Wrong guess a smaller number again
# 6
# Correct, you took 3 trials to guess the number
# Player 2:
# Correct, you took 7 trials to guess the number
#
#    Player 1 wins!
'''
author - Mohammed Irfan
date - 21 April 2022
purpose - fun and practice problem
'''

class players:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # p1 and p2 are names needed to be predefined in the program


    # Takes an input from user of what the player guesses!
    def player_game(self, name, number):
        player = ''
        guess = 0
        while player != number:
            try:
                guess += 1
                player = int(input('\n\tGuess the number:-\t'))
                if player > number:
                    print(f'\tThe number is smaller than {player}')
                elif player < number:
                    print(f'\tThe number is greater than {player}')
                else:
                    print(f'{name} got the answer in {guess} guesses')
                    self.guess = guess

            except:
                print('\tPlease Enter a valid value to guess')

    def winner(self, a, b):
        from random import randint
        number = randint(a, b)        # Chooses a random number from the values given
        number2 = randint(a, b)

        print(f"\t\tNow {self.p1}'s turn to play:-")
        # player1/player2 = self.guess gets 2 different amounts of guesses taken for player1 and 2 to answer correct
        self.player_game(self.p1, number)
        player1 = self.guess

        print(f'\t\tNow {self.p2} is the second player:-\n')
        self.player_game(self.p2, number2)     # number and number2 picks 2 different random values from the range given
        player2 = self.guess

        # Checks for victory of 2 players or tie

        if player1 < player2:
            print(f'\t{self.p1} is winner with a score of {player1} and {self.p2}:{player2}')
        elif player1 > player2:
            print(f'\t{self.p2} is winner with a score of {player1}and {self.p2}:{player2}')
        else:
            print(f'Its a tie between {self.p1} and {self.p2}')


if __name__ == '__main__':
    a = ''
    b = ''
    while type(a) != int and type(b) != int:
        try:
            a = int(input('\n\tEnter the minimum range of number\t'))
            b = int(input('\tEnter the maximum range of number\t'))
        except:
            print('\n\tPlease Enter A Valid Value:\t')
    # Gets the range to generate 2 different random values

    players = players('Irfan', 'Rayhan')
    players.winner(a, b)