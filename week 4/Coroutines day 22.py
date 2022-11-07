import time

# Coroutines are used to initialize the main function which may take a long time and then goes to loop

def searcher():
    print('Function will start in 4 seconds')
    time.sleep(4)   # Can be any sort of time taking task
    book = 'Geronimo, Horse, animals, Dinosaur, Schools are fools'

    while True:
        Text = (yield)  # THis is now a coroutine ALONG WITH WHILE TRUE where its become a generator
        if Text in book:
            time.sleep(1)
            print('YES The book is available in library')
        else:
            time.sleep(1)
            print('Sorry The book you are searching for is not available')


search = searcher()
next(search)        # return the items to an iterator and the actual functions is executed once and
count = 0           # The remaining time it will go to While True loop


while count<10:
    user = input('Please enter what you want to find!\n')
    search.send(user)
    count+=1

search.close()  # Will close the coroutine