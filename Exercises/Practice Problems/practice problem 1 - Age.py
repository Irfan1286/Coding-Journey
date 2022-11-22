#   Problem Statement:-
# Take age or year of birth as an input from the user. Store the input in one variable.
# Your program should detect whether the entered input is age or
# year of birth and tell the user when they will turn 100 years old.

# Here are a few instructions that you must have to follow:
# 1) Do not use any type of module like DateTime or date utils.
# 2) Users can optionally provide a year, and your program must tell their age in that particular year.
# 3) Your code should handle all sorts of errors like :
#       You are not yet born
#       You seem to be the oldest person alive
#       You can also handle any other errors, if possible!

try:
    current_year = int(input('Enter the Current year'))
except:
    current_year = 2022

age_or_birth = input('Enter your age or date of birth in the format DD/MM/YY:-\t')

if age_or_birth.isnumeric():
    year = (100-int(age_or_birth))+current_year

    if year <= current_year:
        print('Wow you are above 100 and might be one of the oldest to be alive')

    elif int(age_or_birth) < 0:
        print('you are not born yet')

    else:
        print(f'you will turn 100 on the year {year}')


elif age_or_birth.count('/') == 2:
    age_or_birth = age_or_birth.split('/')

    if len(age_or_birth[2]) != 4 :
        print('Please enter a valid year')

    elif current_year < int(age_or_birth[2]):
        print('You are not born yet')

    else:
        year = int(age_or_birth[2])+100
        if year <= current_year:
            print('Wow you are above 100 and might be one of the oldest to be alive')

        else:
            age_or_birth.pop(2)
            age_or_birth.append(str(year))
            print(f'you will turn 100 on {"/".join(age_or_birth)}')