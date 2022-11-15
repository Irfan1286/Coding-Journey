# Make a program where the user needs to input The (directory not to change,
# reject renaming Folder and Takes a format of folder to Capitalize

# Summary:
# Take input of full path, a txt file name, and Formats of folder to rename and Capitalize
# The Txt file will contain all names of file where the user doesn't want to Rename and Capitalize

import os

def RenameFile():
    # All The Inputs
    path = input('\tEnter your path where file is located!:\n\t')
    ignore = input('\tEnter the the text file where your names of files are present and you Dont Want to change'
                   '\n\tElse click "Enter" if you want to rename all Files\n\t')
    format_of_file = input('\tPlease ENTER The Formats Of File To Rename:  ')
    what_do = input('\n\tDo You Want to Capitalize or Rename as numbers to the files Type [C],capitalize or [N],number: ')

    # Working using the inputs
    try:
        os.chdir(path)
        try:
            with open(ignore) as file:
                ignore_lines = file.readlines()
                ignore_files = [lines.split('\n')[0] for i,lines in enumerate(ignore_lines)]
        except Exception as j:
            print('\n\tThe file you mentioned is not present in the directory!')
            ignore_files = []   # so that error doesn't come up later in program!

        list_of_file = os.listdir()     # creates a list
        for i,name in enumerate(list_of_file):
            if name not in ignore_files and format_of_file in name:
                if what_do.capitalize() == 'C':
                    os.rename(name, name.capitalize())
                    print(f'Capitalized {name} successfully')

                elif what_do.capitalize() == 'N':
                    os.rename(name, str(i+1))
                    print(f'\tNumbered {name} successfully')

                else:
                    print('Please Enter C or N To run program Successfully, Renaming files failed')
                    break
    except Exception as j:
        print('\t\tPlease Enter A Valid Directory')


if __name__ == '__main__':
    RenameFile()



