#FILE IO
'''
"r" - open and read a file
"w" - open and write on file
"x" - create a file if it doesn't exist
"a" - append more content to file
"t" - text mode
"b" - binary mode
"+" - Read and write on a file
'''

# def func1(a):
#     '''this is doc string'''
# print(func1.__doc__)   #Excercise

f = open('Irfan.txt',"rt")  #rt means read and t means text == read text
print(f)
print('\n', f.read())
f.close()


n = open('Irfan.txt','rt')
print('\n', n.readline())
print('\n', n.readline())  #Read line only reads one line
n.close()   #.close is needed or else it will mess with other statements in python

t = open('Irfan.txt', 'rt')
print('\n', t.readlines(), '\n')      #It will read everything in one statement aka LIST
t.close()

a = open('Irfan.txt', 'rt')
content = a.read()
for scentence in content:
    #print(scentence)
    print(scentence, end = '')
a.close()

try:
    z = open('New file.txt', 'x')
    z.close()
except Exception as k:
    print(k)

# y = open('New file.txt', 'w')
# l = y.write('Humans are the most intelligent being living on earth')
# y.close()

i = open('New file.txt', 'a')
l = i.write('\nHumans are the most intelligent being living on earth')
i.close()

#Handle read and write simultaneously
v = open('New file.txt', 'r+')      #r+ means read and write as well
print(v.read())
v.write('\nThank You')
v.close()


#---------------------------------------------------------------------------------------------------#


f = open('Irfan.txt')
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.close()

u = open('Irfan.txt')
u.seek(24)                      #.seek resets the pointer to the character to start from
print(u.readline())
u.close()

#With block
with open('Irfan.txt') as f:
    print(f.read(8))

#print(f.read(5))   This wont work as with function deletes the need of .close