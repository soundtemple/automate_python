# The hello function is defined
def hello():
    print('Hello there.')

hello()

# A parameter is a variable that an argument is stored in when a function is called.
def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')


# The value that a function call evaluates to is called the return value of the function.
# You can specify what the return value should be with a return statement.
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'


# you can pass return values as an argument to another function call
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
# can be shortened to...
print(getAnswer(random.randint(1, 9)))

# The None Value
# None is the only value of the NoneType data type
# Other programming languages might call this value null, nil, or undefined.


# Keyword Arguments
# Most arguments are identified by their position in the function call.
# However, keyword arguments are identified by the keyword put before them in the function call
print('Hello', end='') #disables carriage return
print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep=',')
# For now, just know that some functions have optional keyword arguments that can be specified
# when the function is called.

