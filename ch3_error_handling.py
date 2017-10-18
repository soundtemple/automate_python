def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument Timmy.')
    except TypeError:
        print('Must use a integer not a string')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
print(spam('string'))


# Errors can be handled with try and except statements.
# When code in a try clause causes an error,
# the program execution immediately moves to the code in the except clause.
# once the execu- tion jumps to the code in the except clause, it does not return to the try clause.
# Instead, it just continues moving down as normal.