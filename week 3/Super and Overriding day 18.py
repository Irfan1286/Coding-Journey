
class X:
    classvar1 = 'This is in class X'
    def __init__(self):
        self.var1 = 'I am in function where self.var = This statement in class X'
        self.number = 78
        self.special = 'I am special'

class Y(X):     # Inherited from class X
    classvar2 = 'This is class Y'
    def __init__(self):
        super().__init__()
        self.var1 = ',Now this is over rided'        # This is overriden so the upper function __init is ignored
        self.name = 'Class Y'
        # IF super is placed on this line, var1 will become the original statement of class X
        # super().__init__()


algebra = Y()

print(algebra.special, algebra.var1, algebra.name)      # Due to super() I was able to access the __init of class X