
def compliment(str):
    return f'{str} is a good boy'

def wrongmath(a, b):
    return a + b + 5

def means(diction):
    for words in diction:
        print(f'{words} means {diction[words]}')


if __name__ == '__main__':          # This is used to avoid things getting an output on another file/CAnt be used on other files
    meanings = {'I': 'Me', 'He': 'Someone else who is a boy'}
    means(meanings)