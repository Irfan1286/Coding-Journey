
# Abstration divides parts Ex: cpu, mouse, moniter,keyboard, gpu, etc makes up a computer so each part is an abstraction
# Encapsulation hides working Ex: how mouse works or how keyboard works (NOT LITERALLY)

# single inheritance copies a class and modifies it does it so we dont need to break the DRY rule/code reuse-bility

#-------------------------------------Single Inheritance-------------------------------------

class Employee:
    company = 'Software company'
    def __init__(self, workers, salary, works):
        self.worker = workers
        self.salary = salary
        self.job = works
    @classmethod        # can modify class across the whole class
    def from_dash(cls, info):
        return cls(*info.split('/'))  # returns info to class


Jack = Employee.from_dash('Jack/55k per year/Product Packing')
Charles = Employee.from_dash('Charles/40k per year/customer service')
Betty = Employee.from_dash('Betty/25k per year/Cooks for employee breaks')


class Programmer(Employee):                 #This is single inheritance, programmer inherited from class employee
    def programmer_details(self):
        return f'The name of the programmer is {self.worker}, and the salary for him will be {self.salary}'


kevin = Programmer.from_dash('Kevin/125k per year/Gui devoloper')
print(kevin.programmer_details())
print(Betty.salary)     #programmer_details cant be used on betty as its assigned from employee
                        # Whereas kevin is assigned to programmer which inherited codes from employee


#-------------------------------------Multi_level Inheritance-------------------------------------

class inherited2(Programmer):           # This is multi level inheritance which comes from programmer and Employee
    # Warning don't repeat this as super can be used I am not using it yet as i didn't learn it
    def __init__(self, name, salary, languages):
        self.name = name
        self.salary = salary
        self.language = languages

    def details(self):
        return (f'Name of programmer is {self.name}, his salary is {self.salary}, and learnt the languages he learnt are {self.language}')


Irfan = inherited2.from_dash('Irfan/150k per annum/[Python, c++]')
print(Irfan.details())


class part_time:
    def __init__(self, name, part_job):
        self.name = name
        self.part_job = part_job

#-------------------------------------Multiple Inheritance-------------------------------------


class full_part_timer(Employee, part_time):        # This is multiple inheritance It will take functions of first variable which is employee then work
    def printdetails1(self):
        detail = f'Name of worker is {self.worker}, whose salary equals to {self.salary}, and works as {self.worker}'
        return detail
    def printdetails2(self):
        detail = f'Name of worker is {self.name}, and part times as {self.part_job}'
        return detail
    def printdetmix(self):
        detail = f'Name of worker is {self.name}, and earns about {self.salary} by working as {self.job} while part timing as {self.part_job}'
        return detail


Tihan = full_part_timer.from_dash(f'Tihan/125k per year/gui devolopment')
Tihan.name = 'Tihan'        # Gets assigned in full_part_timer where
Tihan.working = 'Cook'

print('\n', Tihan.printdetails2())
print('\n', Tihan.printdetmix())





