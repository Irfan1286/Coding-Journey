

class info:
    var = 5     # This is a public variable
    _protected = 10     # This is a protected variable which can be directly accessed through subclass not any
                        # Outside command can override it except for sub-classes/ inherited classes
    __private = 98  # Can't be accessed even with print unless name of class is used so even subclass cant access it

print(info.var)
print(info._protected)
try:
    print(info.__private)
except Exception as h:
    print("__private could not be printed")

print(info._info__private)      # to print private variable we need to use the name of class

# *Note :: Name doesn't matter to assign them only __ or _ name matters
# This is name angling

#-------polymorphism-------

print(10+8)
print('10'+'8')     # this is polymorphism