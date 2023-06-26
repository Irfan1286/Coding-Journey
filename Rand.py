#1 Splitting, multiplying, typecasting
user = input("Please enter your numbers to multiply with a colon in between them\n")
x = user.split(":")     #Creates a list of numbers seperated by the colon

total = len(x)
result = 1          #done to avoid "the name result is not defined" error

for i in range(total):
    x[i] = int(x[i])        # typecasts to integers
    result = result * x[i]  

print(result)

#2 Adding variable to a blank dictionary
new = {}
new['snack'] = 'chips'      # new.update({'':''}) could also be used
print(new)


#3 Naming numbers
print('3) Naming Numbers')

numdict = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
           10:'ten', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 
           100:'hundred', 1000:'thousand'}


# usernum = int(input('Enter Your Number:\t'))
usernum = result


if usernum in numdict:
    print(numdict[usernum])
    
else:
    # for number in numlist:
    #     if number < usernum:
    #         max = numlist[number]
    #         print(max)
    # tb
            
        
    charlist = list(str(usernum))   # creates a list of characters like, "2", "5", "9"
    digits = len(charlist)
    
    for n in range(digits):
        charlist[n] = int(charlist[n])    # converts string list to integer list
    print(charlist)   
    
    # Write a func
    def namethem(index, zero):
        '''Docstring:- Names the digits'''
        if zero != True:
            part = numdict[ charlist[index] ]
        else:
            part = numdict[ int(str(charlist[index])+'0') ]
        return part
        
    if digits == 7:
        print(namethem(0, False),'Million', namethem(1, False), 'hundred and', namethem(2, True), namethem(3, False),'thousand', namethem(4, False),'hundred and', namethem(5, True), namethem(6, False))
    
    elif digits == 6:
        print(namethem(0, False),'hundred and', namethem(1, True), namethem(2, False),'thousand', namethem(3, False), 'hundred and', namethem(4, True), namethem(5, False))

    elif digits == 5:
        print(namethem(0, True), namethem(1, False),'thousand', namethem(2, False), 'hundred and', namethem(4, True), namethem(5, False))
    
    elif digits == 4:         #thousands
        print(namethem(0, False), 'thousand', namethem(1, False), 'hundred and', namethem(2, True), namethem(3, False))

    elif digits == 3:       #hundreths ex 433
        print(namethem(0, False),'hundred and', namethem(1, True), namethem(2, False))

    elif digits == 2:       #tens  ex 24
        # key:value
        print(namethem(0, True), namethem(1, False))

