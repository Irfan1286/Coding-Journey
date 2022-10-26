class position:
    place = 'Samsung'
    def printdetails(self):                         #self will be automatically filled in brackets
        print(f'His name is {self.name}, Who has a salary of {self.salary}, and manages {self.role} in Samsung devices')

Irfan = position()
Harry = position()

Irfan.name = 'Irfan'
Harry.name = 'Harry'

Irfan.salary = '130 lpa'
Harry.salary = '95 lpa'

Irfan.role = 'backend software developing'
Harry.role = 'good battery life'

print(Irfan.printdetails())     # the name.function in print will decide for the details
print(Harry.printdetails())


class student:
    school = 'PBGS (prime bank grammar school'
    def __init__(self, name, id, grade, timings):
        self.name = name
        self.id = id                    # __init__ is a constructor
        self.grade = grade
        self.timings = timings

    def details(self):
        print(f'His name is {self.name} and studies in grade {self.grade}')
        print(student.__dict__)   # This will give unnessary info in function of a class

Tihan = student('Tihan', '00969', 10, '9:00am to 1:00pm')       # The arguments will automatically go into init
Rayhan = student('Rayhan', '00971', 6, '9:00am to 1:00pm')

print('\n', Tihan.id)
print(Rayhan.details())
print('\n', Tihan.__dict__)

