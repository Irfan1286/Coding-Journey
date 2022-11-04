# Create a library class
# show all the books present in library
# Show all the books that were lend from library    and who took the book
# people must be able to donate/Add books to library
import time


# The constructor must take in list_of_books and library_name
# create a main function and run an infinite while loop asking user for input

class library:
    def __init__(self, list_books, library_name):
        self.books_avail = list_books
        self.libraryname = library_name

    def diplay(self):
        book_file = str(self.books_avail)
        with open(book_file) as L:
            for i in enumerate(L):
                print(i)
        L.close()

    def lend(self):
        borrow = int(input('Write the serial numbers of the book you want to borrow'))
        username = input('Please also type in your username')
        book_file = self.books_avail

        with open(book_file, 'r') as f:
            data = f.readlines()

        with open(book_file, 'w') as file:
            for i , line in enumerate(data):
                if i == borrow:
                    if '  ----->' in line:  # checks if book is already taken
                        x = line.split('>')     # splits after >
                        x = x[1].split(',')         # creates a list after , where the name of user who took it is stored
                        print(f'Sorry This book is taken by{x[0]}')
                        file.writelines(line)   # rewrites the same line again
                    else:
                        x = line.replace("\n", '')  # Replaces \n so that the next line goes on same line
                        file.write(f'{x}  -----> {username}, has borrowed the book! ')
                        file.write('\n')    # Adds the \n again to seperate the line and next line
                        print(f'you have taken the book [{x}]')
                else:                           # Write is used to write only a single string
                    file.writelines(line)       # Writelines is used to write a list of string to a opened file

    def give_back(self):
        user = int(input('the serial number of book you want to return'))
        library_books = self.books_avail
        name = input('Please enter the name with which you have borrowed')

        with open(library_books) as book:
            data = book.readlines()
        with open(library_books, 'w') as file:
            for i, line in enumerate(data): # i is the line its representing and line is a list taken from the read data
                if i == user:
                    if '  ----->' in line and name in line:
                        x = line.split('  -')   # gap gap split so that a gap isnt left back everytime
                        file.write(x[0])
                        file.write('\n')
                        print(f'\n\tYou Have returned [{x[0]}] successfully!')
                    else:
                        file.writelines(line)
                        print('Sorry ! You did not take the book or it was not taken')
                else:
                    file.writelines(line)
    def Add(self):
        lib = self.books_avail
        book = input('Type name of book you want to add')
        with open(lib, 'a') as file:
            file.write('\n')
            file.writelines(book)
            print('you have successfully added the book', book)

def func1(num):
    if num == '1':
        from time import sleep
        geronimo.diplay()
        time.sleep(5)
    elif num == '2':
        geronimo.lend()
    elif num == '3':
        geronimo.give_back()
    elif num == '4':
        geronimo.Add()

if __name__ == '__main__':
    geronimo = library('Geronimo books.txt', 'Geronimo Stilton')
    choice = None
    while choice != 'End':
        print('\nEnter one of the following number \n1) Display library \n2) Borrow book from library '
              '\n3) Return book to library \n4) Add or Donate A book To Library \n5) Multifunction'
              '\n\t Or Type "End" to QUIT')
        choice = input().capitalize()
        func1(choice)
        if choice == '5':
            user_func = input('Enter the number of functions to run and use x to repeat Multiple times :  ')
            x = user_func.split(' ')
            for element in x:
                if 'x' in element:
                    from time import sleep
                    z = element.split('x')
                    for i in range(int(z[1])):
                        func1(z[0])
                        time.sleep(2)
                else:
                    func1(element)

