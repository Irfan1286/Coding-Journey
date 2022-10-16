# i = 0
#
# while (i<=20):                       #conditions needs to be given in brackets
#     print(i)
#     i = i + 1


p = 0
while (True):                       #True means it will run for eternity or use "While p>=20"
    if p<5 :
        p = p + 1
        continue
    print(p + 1, end=', ')
    p = p + 1
    if p>=20:
        break


print('\n\tyour loop is finished')
