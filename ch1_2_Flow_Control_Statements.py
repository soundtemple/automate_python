print('Hello world!')
# Python is calling the print() function
# The string value is being passed to the function.
# A value that is passed to a function call is an argument.

myName = input()
# This function call evaluates to a string equal to the user’s text, and the
# previous line of code assigns the myName variable to this string value.

print(len(myName)) # evaluates to an integer.

str(29) 
# concatenate strings and integers by converting integer to a string
# The str(), int(), and float() functions will evaluate to the
# string, integer, and floating-point forms of the value you pass, respectively.
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

# Different types of operators (+, -, *, /, //, %, and ** for math operations)
# + and * for string operations  eg: 'Timmy'*3

# Data Types: Integer, Float, String

# Flow control statements can decide which Python instructions to execute under which conditions.
# Data Type: Boolean - only two states

# Comparison operators compare two values and evaluate down to a single Boolean value.
== != < > <= >=
# The == and != operators can actually work with values of any data type.

# The three Boolean operators
and or not
# and evaluates to True only if both conditions are True
# or evaluate to True if one of the conditions are True
# not operator simply evaluates to the opposite Boolean value
(1 == 2) or (2 == 2)

# Flow Control Statements
# An if statement’s clause (that is, the block following the if statement)
# will execute if the statement’s condition is True.
if name == 'Alice':
    print('Hello, Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('Hello, stranger.')

# When there is a chain of elif statements, only one or none of the clauses will be executed.
# Once one of the statements’ conditions is found to be True,
# the rest of the elif clauses are automatically skipped.

# The code in a while clause will be executed as long as the while state- ment’s condition is True.
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

# while True => infinite loop. Use if break to exit
while True:
print('Please type your name.')
name = input()
if name == 'your name':
    break print('Thank you!')

# continue and break
# the continue statement causes the program execution to jump back to the start of the loop.
while True:
   print('Who are you?')
   name = input()
   if name != 'Joe':
       continue # back to while
   print('Hello, Joe. What is the password? (It is a fish.)')


# Truthy & Falsey
# When used in conditions, 0, 0.0, and '' (the empty string) are considered False,
# while all other values are considered True.
while not name:
if numOfGuests:


# Range method takes (start, end, jump)
for i in range(5):
    print(i)

# Module import  (NB: Dont name files with a keyword eg random.py)
import random
print(random.randint(1, 10))


