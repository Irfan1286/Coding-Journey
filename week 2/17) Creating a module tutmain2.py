import tutmain17

try:
    print(tutmain17.means(tutmain17.meanings))
except Exception as r:
    pass                    # This won't work as the meanings variable are inside [if __name__ == '__main__']

dictionary = {'short':'Relatively small', 'extinct':'species that are not available anymore'}
print(tutmain17.means(dictionary))
print(tutmain17.wrongmath(2, 4))
print(tutmain17.compliment('Irfan'))
