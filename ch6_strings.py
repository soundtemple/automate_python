# Escape Characters
# \'    Single quote
# \"    Double quote
# \t    Tab
# \n    Newline (line break) 
# \\    Backslash

print('hello')
print('\'\"\t\n\\')
print('Say hi to Bob\'s mother.')

# Raw Strings
print(r'Say hi to Bob\'s mother.')


# Multiline Strings
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,

Bob''')

# Indexing strings
spam = 'Hello world!'
spam[:5]
spam[6:]
fizz = spam[0:5]
# fizz = 'Hello'


# The upper(), lower(), isupper(), and islower() String Methods
# The isupper() and islower() methods will return a Boolean True value
spam.islower()

# See also. These return boolean
isalpha()
isalnum()
isdecimal()
isspace()
istitle()


# eg:
while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

# The startswith() and endswith() String Methods
'Hello world!'.startswith('Hello')
'Hello world!'.endswith('world!')


# The join() and split() String Methods
'_'.join(['My', 'name', 'is', 'Simon']).lower()

remove_line_breaks = '''Dear Alice,
How have you been? I am fine. There is a container in the fridge that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''

' '.join(remove_line_breaks.split('\n'))


# Justifying Text with rjust(), ljust(), and center()
'Hello'.rjust(10)
' c e n t e r '.center(50)

# An optional second argument to rjust() and ljust() will specify a fill character other
#  than a space character. Enter the following into the inter- active shell:
'Hello'.rjust(20, '*')
'Hello'.center(20, '=')

# cool example
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)


# Removing Whitespace with strip(), rstrip(), and lstrip()
# The lstrip() and rstrip() methods will remove whitespace
# characters from the left and right ends, respectively.

'wxyzTEST_TIMMYwxyzwxyz'.strip('wxyz')


# Copying and Pasting Strings with the pyperclip Module
import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()

