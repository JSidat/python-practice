my_pets = ['zophie', 'pooka', 'fat-tail']
name = input('enter name here: ')
if name not in my_pets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
