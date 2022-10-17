z = 94      # This is a global variable

def glocal():
    try:
        z += 20
    except Exception as d:
        print(d)
    print('z cant be added as its a local variable in this function so permission needs to be given')
    print('The Permission can be given using Global function')

print(z)

glocal()

def works():
    global z
    z += 2
    print(z, 'THis was possible due to given permission')

works()

n = 50
def variable():
    n = 5           #This is a local variable
    print(n)
variable()


c = 10
def new():
    print('entered 1st function')
    def new2():
        print('Entered second function')
        global c
        c += 20
    print('before calling new2', int(c))
    new2()
    print('After Calling new2', int(c))



new()
print(c)

