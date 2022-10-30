

class Account:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property       # To get rid of brackets during something.email() we use property
    def email(self):
        if self.fname == None or self.lname == None:
            return 'Please set your email Using Setter, and try again Later'
        return f'Your email is :\n{self.fname}.{self.lname}@python.com'

    @email.setter   # Allows to set things/ Modify outside class
    def email(self, string):
        print('Setting Your Email Now...')
        names = string.split('@') [0]   # Creates a list where Everything after @ is ignored
        self.fname = names.split('.') [0]       # It will split names where . is present into first index
        self.lname = names.split('.') [1]       # It will split and store after . in next index

    @email.deleter      # allows to delete when del function is used
    def email(self):
        self.fname = None
        self.lname = None


Irfan = Account('Irfan', 'Best')
print(Irfan.email)      # to get the desired format instead of rubish main bla bala we used property decorator

Irfan.email = 'tihan.ben'       # First it will go to setter then to email property
print(Irfan.email)

del Irfan.email
print(Irfan.email)

