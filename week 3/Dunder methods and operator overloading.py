

class home:

    # This is a dunder method also!
    def __init__(self, location, distance):
        self.address = location
        self.distance = distance

    # This is an overloading operator. other will search for all integers assigned in self
    def __add__(self, other):
        return self.distance + other.distance

    # __something__ are dunder methods including int
    def __sub__(self, other):
        return self.distance - other.distance

    def __truediv__(self, other):       # This is also a dunder method
        return self.distance / other.distance

    def __repr__(self):          # This is also a dunder method
        return f'Address of Home is "{self.address}" and it is "{self.distance}" meters away from you'

    def __str__(self):      # This is also a dunder method
        return f'Location is {self.address} and its {self.distance} meters far'


Address1 = home('Azampur kacha bazar, Right side jamtola , dakshinkhan, House no 57', 2265)
Address2 = home('school', 100)


print(Address1 + Address2)      # + will be overided to __add__ function where distance is added
print(Address1 - Address2)      # same will happen here but - will go to __sub__
print(Address1 / Address2)      # / will be overided with __truediv__

print(Address1)         # Due to __repr__ this is coming to a desired format instead of <__main__.home object at 0x0000029ABFD47E20>
print(repr(Address2))          # But print statements likes to take __str__ dunder to print. Try commenting the __str__ dunder

# normally repr doesn't need to be used unless there is __str__ method

# To search for more overiding operators type mapping operators python in google