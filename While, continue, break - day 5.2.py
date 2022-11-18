# i = 0
#
# while (i<=20):                       #conditions needs to be given in brackets
#     print(i)
#     i = i + 1


p = 0
while (True):                       #True means it will run for eternity or use "While p>=20"
    if p<5 :
        p = p + 1
        continue    # Won't allow rest of program to run until the if condition is true
    if p>=20:
        break
    print(p + 1, end=', ')
    p = p + 1

print('\n\tyour loop is finished')
