
#F strings stand for fast string
# to use it we use f before giving the string in ""

p = 'pepsi'
z = 'coca-cola'
print('Is', z, 'better or, is', p, 'better?')   #this is really an inefficient way and not clear to read

print(f'Is {z} better or is {p} better?')   # Due to the f  string we can understand where are variables are printing more clearly

#--------------------------------------------------------------------------------------------------
# JOIN Function!

jobs = ['software engineer', 'Builder', 'Chef', 'Doctor', 'Accountant', 'Waiter']

# for profession in jobs:
#     print(profession, end=', ')       #Instead

a = ', '.join(jobs)             # This will also give same result as for loop and
                                # \n can be used in string to print in sequence
print(a, 'Are all good jobs to apply for')