#Create a program where there are 4 words in a dictionary,takes input from user and
# return the meaning of the word from dictionary
print('Welcome to dictonary',
      '\nyou can search for following terms'
      '\n mutable','\n medicine', '\n solar', '\n Homeless')

means = {'mutable':'it can be changed or modified as required',
         'medicine':'used to cure living beings',
         'solar':'Energy from Sun', 'Homeless':'someone without home'}

user = str(input())
print(user, ":means", means[user.lower()])