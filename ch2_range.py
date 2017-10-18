print('My name is')
for i in range(5):
    print('Your name is ' + str(i) + ' Timmy')

# add all numbers 0-100
total = 0
for num in range(101):
    total = total + num
print(total)
# The for loop v then executes total = total + num w 100 times.

# 5 iterations from 0-4 inclusive
for i in range(5):
    print(i)

# 12 - 15
for i in range(12, 16):
    print(i)

# jump in 3's 21 not included
for i in range(0, 21, 3):
    print(i)

# negative 
for i in range(5, -1, -1):
    print(i)