

class learn:
    def __init__(self, subject, learning, interest):
        self.subject = list(subject.split(','))
        self.learning = list(learning.split(','))
        self.interest = list(interest.split(','))

    @property
    def Master(self):
        return f'You should focus on your {",".join(self.interest)} more than {self.learning}'

Irfan = learn('Maths, English, Science, Bangla, Computer Science', 'Bangla', 'Python, Football')

print(Irfan.Master)

print(dir(Irfan))   # shows all possible codes to use with the object
print(id(Irfan))     # id will be different everytime
print(type(Irfan))  # Above 2 and this is a type of object introspection

import inspect
print(inspect.getmembers(Irfan))

