# json = Java-Script Object Notation

import json

# ---------------------> Json to python
data = '{"var1":"Irfan", "var2":34}'    # This is a string in json, so It is not considered as a list
print(data)                             # That's why ['var1'] cant be used

parse = json.loads(data)                # This is a list now which has been Converted from a string
print(parse['var1'])                    # This is a list due to which [var1] con be used

dict1 = {
    'food': ('Pasta', 'Juice', 'Bread', 'Burger'),
    'cars': ['BMW', 'Ferrari', 'Lamborghini', 'Toyota'],
    'is Bad?': False,    # False cant be used in javascript as it is false in javascript
    'Number' : ('ONE', 1)
}

# ----------------------> Python to json

print(json.dumps(None))

java_compatible = json.dumps(dict1)         # .dumps makes it java compatible
print(java_compatible)      # See, IS bad variable will be turned to small letter false which is used in java
                            # Also the tuple is converted to list


                    # Sorts the list alphabetically
java_compa2 = json.dumps(dict1, indent=5, sort_keys=True)   # indent means How many indents to use to make look better
print(java_compa2)                          # Prioritizes Capital letters instead of small letters First


#-----------------------------> Json.load (reading json file)

with open('for json module day25.json') as f:
    x = json.load(f)
    print(x)

