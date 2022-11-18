# Task - Make an email collector from a string using re (regular expressions module)

import re

email = '''
These are sample email addresses 

Google
google123@gmail.com

facebook
facebook45@gmail.com

sample mail.io
samplemail.io.98789@gmail.com

jetbrains
pyhton_jetbrains@gmail.com

software.jk@gmail.com

horsify#453@gmail.com

gamenote@yahoo.com

twitter.co@gmail.com

account.generator@gmail.com

school
pbgs123@gmail.com



contact = +7068768768700
for more info contact at kingmen@gmail.com
tech_support - tech_support@gmail.com

'''

Accounts = re.findall(r'[\w.]+@[\w.]+', email)   # This will give list where the pattern(account ids) will be stored
# \w matches word character and \. takes the rest of the characters and the brackets
# make it so that it's a set of characters and searches for where @ is present and + means only that much is needed

# matches = re.findall(r'[\w\.]+@[\w\.]+', email)  # finditer will give re.match object


for items in Accounts:
    try:
        with open('Gmail Accounts.txt', 'x') as f:
            f.writelines(f'{items}\n')

    except:
        with open('Gmail Accounts.txt', 'a') as f:
            f.writelines(f'{items}\n')

    finally:
        print(items)
print('Accounts Have been dumbed successfully into Accounts.txt')


