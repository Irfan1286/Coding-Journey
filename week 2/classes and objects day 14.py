# classes - Template
# objects - instance of classes

# RULE
# DRY - do not repeat yourself

class student:
    pass

Irfan = student()           # both of the variables are different
rayhan = student()          # the brackets means that objects can go into the variable
print(Irfan, rayhan)        # both objects are different

Irfan.nickname = 'Tihan'
Irfan.standard = 10
Irfan.age = 16
print(Irfan.nickname, Irfan.standard, Irfan.age)

rayhan.nick = 'ayan'
rayhan.std = 6
rayhan.age = 11
print(rayhan.nick, rayhan.std, rayhan.age)

print(rayhan.__dict__)
print(Irfan.__dict__)           # This prints everything assigned in Irfan


class job:
    working_place = 'microsoft'
    pass

harry = job()
rohan = job()       # everything in job will be shared except for their personal values such as salary
Irfan = job()

harry.salary = '45 lpa'
rohan.salary = '32 lpa'     # Rohan is an instance whereas job() is a class
Irfan.salary = '46 lpa'

Irfan.role = 'Senior backend developer'
harry.role = 'Senior backend developer '
rohan.role = 'Senior Gui frontend developer'

print(harry.working_place)

rohan.working_place = 'google'                  # This only changes for rohan to change universally use job.working_place
print(harry.working_place,Irfan.working_place, rohan.working_place)

job.working_place = 'Amazon'                    # but for rohan it stays google
print(harry.working_place, Irfan.working_place, rohan.working_place)



