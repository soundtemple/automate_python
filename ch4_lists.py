# Lists
# A list is a value that contains multiple values in an ordered sequence.
# The term list value refers to the list itself

spam = ['cat', 'bat', 'rat', 'elephant', ['cat', 'bat']]

print(spam[0])
print(spam[4][1])
print(spam[-1])
print(spam[1:4])  # returns 1,2,3 not 4
print(spam[1:])  # ignoring integer uses defaults [0:-1]
spam[0] = 'timmy'
print(spam[0])

# List  concatenation  (+ & * Operators)
[1, 2, 3] + ['A', 'B', 'C']
['X', 'Y', 'Z'] * 3


# Deleting
spam = ['cat', 'bat', 'rat', 'elephant'] 
del spam[2]

# Lists and Loops
print('*********  LIST LOOPS *****')
supplies = [1,2,3,4,5,'poo']
for i in range(len(supplies)):
    print(supplies[i])



# The in and not in Operators
# You can determine whether a value is or isn’t in a list with the in and not in operators.
# These expressions will evaluate to a Boolean value.
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam
'cat' in spam
'cat' not in spam

if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

# Multiple assignment trick
cat = ['fat', 'black', 'loud']
size, color, disposition = cat


# Augmented assignment statement
spam += 1
spam -= 1
spam *= 1
spam /= 1
spam %= 1

# List Data Type - Method
spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')

list.index()  # find in list. returns first value found
list.append() # adds to end of list
list.insert(1, 'elem') # position and element
list.remove()
list.sort(reverse=True) # cant sort letters and numbers. ASCII sort caps come first
list.sort(key=str.lower) # sorts ignoring case


# You can also split up a single instruction across multiple lines using the \ line continuation character
# at the end. Think of \ as saying, “This instruction continues on the next line.”


# List-like Types: Strings and Tuples
# Many of the things you can do with lists can also be done with Strings.
>>> name = 'Zophie'
>>> name[0]
'Z'
>>> name[-2]
'i'
>>> name[0:4] 'Zoph'
>>> 'Zo' in name True
>>> 'z' in name False
>>> 'p' not in name False
>>> for i in name:
        print('* * * ' + i + ' * * *')

# Mutable and Immutable Data Types
# A list value is a mutable data type: It can have values added, removed, or changed.
# However, a string is immutable: It cannot be changed.
# Trying to reassign a single character in a string results in a TypeError error

# Tuples
# The tuple data type is almost identical to the list data type, except in two ways.
# First, tuples are typed with parentheses, ( and ), instead of square brackets, [ and ].
# Tuples, like strings, are immutable. IE Tuples cannot have their values modified

# If you have only one value in your tuple,
# you can indicate this by placing a trailing comma after the value inside the parentheses.
>>> type(('hello',)) <class 'tuple'>
>>> type(('hello')) <class 'str'>

# Converting a tuple to a list is handy if you need a mutable version of a tuple value.
>>> tuple(['cat', 'dog', 5]) ('cat', 'dog', 5)
>>> list(('cat', 'dog', 5)) ['cat', 'dog', 5]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']