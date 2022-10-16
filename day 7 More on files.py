
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