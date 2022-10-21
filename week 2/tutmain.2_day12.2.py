import tutmain1

try:
    print(tutmain1.means(tutmain1.meanings))
except Exception as r:
    pass                    # This won't work as the meanings variable are inside [if __name__ == '__main__']

dictionary = {'short':'Relatively small', 'extinct':'species that are not available anymore'}
print(tutmain1.means(dictionary))
print(tutmain1.wrongmath(2, 4))
print(tutmain1.compliment('Irfan'))
