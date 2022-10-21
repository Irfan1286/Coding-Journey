shop = ['tomato', 'jam', 'brush', 'toothpaste', 'toys', 'pillow', 'chicken']

count = 1
for i in shop:
    if count%3 != 1:
        print(f'Jarvis please buy {i}')     #the count%3 != 1 means that ramainder should be equal to 1 to print
        print(count % 3, 'skipped')
    count += 1

print('\n')

for number, item in enumerate(shop):            # Here the count is starting from 1 unlike previous asssigned value
    if number%3 != 0:
        print(f'I need to buy {item}')