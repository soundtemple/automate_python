import copy

spam = [1, 2, 3]


# Passing references
def eggs(someParameter):
    spam2 = someParameter
    print('this is spam2 ' + str(spam2))

eggs(spam)
print(spam)


# Even though spam and someParameter contain separate references, they both refer to the same list.
# This is why the append('Hello') method call inside the function affects the list
# even after the function call has returned.
# Keep this behavior in mind: Forgetting that Python handles list and dictionary variables this way
# can lead to confusing bugs.


# Copy Module
# copy.copy(), can be used to make a
# duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference
letters = ['A', 'B', 'C', 'D']
cheese = copy.copy(letters)
cheese[1] = 42
print(letters)
print(cheese)

# Practice Project - Comma Code

sep_this = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(some_list):
    some_list[-2] = 'and'
    for i in some_list:
        print(i, end=", ")

comma_code(sep_this)


