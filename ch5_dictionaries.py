# Dictionaries
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size']

info = 'My cat has ' + myCat['color'] + ' fur.'

birthdays = {'Alice': '060606', 'Elke': '100829', 'Lily': '070712', 'Tim': '900308'}

print('********  KEYS ********')
for k in birthdays.keys():
    print(k)

print('********  VALUES ********')
for b in birthdays.values():
    print(b)
print('********  ITEMS ********')
for i in birthdays.items():
    print(i)  #tuple
    print(list(i))  #true list
for k,v in birthdays.items():
    print('Key: ' + k + ' Value: ' + str(v)) #key value pairs


print('Alice' in birthdays.keys())
print('Alice' not in birthdays.keys())  #dont really need .keys()
print('Alice' in birthdays)  #checks keys not values

# the get() method
print('The get method takes two arguments ' + str(birthdays.get('nokey', 'not known')) + ' so you have a fallback')

# setdefault() method sets a default value if no value exists
birthdays.setdefault('Dad', '450708')
birthdays.setdefault('Dad', 'XXXXXX')
print(birthdays)

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I dont have a bday for ' + name)
        print('What is their bday? yymmdd')
        bday = input()
        birthdays[name] = bday
        print('Bday database updated.')

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))