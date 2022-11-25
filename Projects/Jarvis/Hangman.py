import random

words = ['alien', 'fever', 'mansion', 'people', 'gigantic', 'joker', 'python', 'hangman', 'delete', 'forever', 'biology', 'chemistry', 'science', 'hangman', 'computer', 'cake', 'height', 'question', 'answer', 'robot', 'queen', 'mystery', 'chair', 'castle', 'elephant', 'orphan', 'desire', 'marvel', 'elements', 'xray', 'animal', 'plane', 'source', 'life', 'archer', 'warrior', 'power', 'speed', 'strength']

body = ['l.arm', 'r.arm', 'r.leg', 'l.leg', 'Head and body']


def get_word():
    word = random.choice(words)
    word = word.upper()
    letters = []
    for i in range(len(word)):
        letters.append(word[i])

    count = 0
    guess = []          # BLANK CANT BE KEPT ABOVE THE WHILE LOOP ELSE IT WILL INCREASE THE INDEX OF LIST
    while count < 5:

        user_letter = input('Guess the letter\n').capitalize()
        guess.append(user_letter)
        blank = []
        for i in letters:
            if i in guess:
                blank.append(i)
            else:
                blank.append('__ ')
        print(' '.join(blank), '\n')

        if user_letter not in letters:
            print(f'The {body[count]} of Hangman is Destroyed')
            count += 1

        if blank == letters:
            print('Victory!!!')
            break
    print(word)

get_word()
