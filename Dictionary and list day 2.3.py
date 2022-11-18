#DICtionary contains pair of values and is made using {}

Grocery = {'food':['burger', 'ketchup'], 'art':'paint'}
print(Grocery['food'])

new = Grocery.copy()
# if .copy is not used then any edit to new will make edit to original
 #Same goes for list and dictionaries

new['tech'] = ['computer', 'cpu', 'mouse']
del new ['art']
new.update({'snack':'Chips'})
print(new)
print(Grocery)

# ----------------------------------Future me--------------------------------------
# To print specific thing from the key and also in dictionary the default value is like [key:value]

print(f'\nFuture Me Adding notes')

for key,value in Grocery.items():       # .items allows to use key and value ; also key and value can be named anything
    print(key)


Grocery.pop('art')  # Deletes the key and the value that comes along with it
print('\n', Grocery)

Grocery.update({'Cars':'Bmw'})    # Can add a new element
print(f'\n{Grocery}')

Grocery.update({'food':'Pizza'})  # or change the previous element
print(f'\n{Grocery}')

print(Grocery.get('Cars'))      # Can be done instead of doing Grocery[Cars]

print(Grocery.clear())      # None will be returned as the Dictionary is cleared
