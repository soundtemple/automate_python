while True:
    print('Who are you?')
    name = input()
    if name.lower() != 'tim':
        continue #back to while
    print('Hello, ' + name + ' What is the password? (Hint: Daughter Flower)')
    password = input()
    if password.lower() == 'lily':
        break
print('Access granted, ' + name)

