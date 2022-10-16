#Sets
# Sets will only contain unique values! THis is what is differnt in sets and lists
# set function can only accept one argument in it

Level = ['Easy', 'Medium', 'hard'] #List
s = set(Level) # Here the list is becoming a Set
s.add('hard')       # A value cant be repeated in sets
s.add('Extreme')
d = s.copy()
d.add(25)
d.add(68)
d.union(s)
print(s)
print(d)
