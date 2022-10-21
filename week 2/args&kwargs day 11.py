
# args means arguments
# *variable means arguments/*args

def funcarg(*args):
    print(*args)
    return

funcarg('a', 1 , 2)

def argsoptional(*args):
    print(*args)

argsoptional() #in args giving an argument is not neccessary


def args(normal, *variable):
    print(normal, *variable)        # the *varible is a argument as it comes after *
    return                          # The normal variable needs to be before the args

args('this is normal,', 'this is an argument which was not neccessary to input')

def kwargs(normal, *args, **kwargs):
    print(normal, *args, **kwargs)          #The kwargs/** is the only thing that can come after an argument!
    return

kwargs('norm', *',*args variable can be anything')

def practice(norm, *names, **optional):
    print(norm)
    for item in names :
        print(item, end=' ')            #While writing in after an args * is not needed
    for people, job in optional.items():
        print(f'{people} is a good {job}')      #for some reason only dictionary worked should try more ** later


name = ('Irfan', 'Harry', 'Jack', 'Tom', 'Jerry')
profession = {'Harry':'Programmer', 'jack':'Plumber', 'Tom':'Cat'}

practice('These are the students:\n', *name, **profession)        # *is needed in args also in printing the function

