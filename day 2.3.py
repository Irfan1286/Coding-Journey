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