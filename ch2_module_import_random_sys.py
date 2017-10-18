# dont name files with keywords!!

import random, sys, copy



# random numbers from 1-10 inclusive
for i in range(5):
    print(random.randint(1, 10))


# sys module to exit a program
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
     sys.exit()
    print('You typed ' + response + '.')