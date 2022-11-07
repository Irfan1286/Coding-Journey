
print('Running')

try:
    with open('TRY.txt') as j:
        print(j.readlines())
except Exception as f:
    print('The problem is', f)

except IOError as h:        # we can use multiple except statements
    print(h)

else:       # Else in try except will only work if try works and except doesn't
    print('THis will only run if except wont work')


finally:     # Statements in This will always execute no matter if try, except or else executes
    print('This will run anyway....')
print('ENDING Program')

