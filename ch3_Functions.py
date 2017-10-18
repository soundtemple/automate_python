# CH3 FUNCTIONS
def hello():
    print("hello")

# A parameter is a variable that an argument is stored in when a function is called.
# Keyword arguments are identified by the keyword put before them in the function call.

# Local vs Global Scope
# Parameters and variables that are assigned in a called function are said
# to exist in that function’s local scope.
# Variables that are assigned outside all functions are said to exist in the global scope.
# While using global variables in small programs is fine, it is a bad habit to rely on
# global variables as your programs get larger and larger.


# The global Statement
# If you need to modify a global variable from within a function, use the global statement.

def spam():
    global eggs #global variable
    eggs = 'spam'

eggs = 'global'

# There are four rules to tell whether a variable is in a local scope or global scope:
# 1. If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.
# 2. If there is a global statement for that variable in a function, it is a global variable.
# 3. Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
# 4. But if the variable is not used in an assignment statement, it is a global variable.

# Error Handling
# See error_handling.py
