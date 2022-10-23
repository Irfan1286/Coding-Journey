jobs = ['software engineer', 'Builder', 'Chef', 'Doctor', 'Accountant', 'Waiter']

# for profession in jobs:
#     print(profession, end=', ')       #Instead

a = ', '.join(jobs)             # This will also give same result as for loop and
                                # \n can be used in string to print in sequence
print(a, 'Are all good jobs to apply for')