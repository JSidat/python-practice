# dictionaries are composed of key-value pairs

myCat = {'size': 'fat', 'colour': 'black', 'disposition': 'loud'}

print(myCat['size']) # the value for the key 'size' is accessed like this

# dictionaries can also use numbers as keys

spam = {1234: 'hello', 123: 'bye'}

# Dictionaries vs lists

dict_1 = {first: 1, second: 2, third: 3}
dict_2 = {second: 2, first: 1, third: 3}


# dict_1 and dict_2 are the same as the order of the key-value pairs in dictionaries do not matter


# dictionaries can be useful to store organised information

birthdays = {'Alice': 'Apr 2', 'John': 'Nov 13', 'Sam': 'Feb 13'}

while True:
    name = input('Enter name here: (blank to quit)')
    if name == '':
        break

    if name in birthdays:
        print(name + "'s" + 'birthday is on ' + birthdays[name])
    else:
        print('I do not have a birthday for ' + name)
        bday = input('Enter ' + name + "'s" + 'birthday here: ')
        birthdays[name] = bday
        print('Birthday database updated')
        print(birthdays)

# The keys(), values(), and items() methods

birthdays = {'Alice': 'Apr 2', 'John': 'Nov 13', 'Sam': 'Feb 13'}

for v in birthdays.values():
    print(v) # will return the values of the key-value pairs in the dictionary

for k in birthdays.keys():
    print(k) # will return all the keys of the key-value pairs in the dictionary

for i in birthdays.items():
    print(i) # will return a tuple of the key-value pairs in the dictionary i.e. ('alice', apr 2, 'john', 'Nov 13, etc...)
    print(list(birthdays.keys())) # this will print the key-value pairs in a list [('Alice', 'Apr 2'), ('John', 'Nov 13'), ('Sam', 'Feb 13')]

for k, v in birthdays.items():
    print('Key: ' + k + 'Values: ' + str(v)) # will return the key-value pairs with labels provided

# checking whether a key-value pair is in the dictionary

birthdays = {'Alice': 'Apr 2', 'John': 'Nov 13', 'Sam': 'Feb 13'}

'Alice' in birthdays.keys() # will return True as 'Alice is a key in the dictionary 

'Nov 14' in birthdays.values # will return False as this value is not present in the dictionary

# The get() method

birthdays = {'Alice': 'Apr 2', 'John': 'Nov 13', 'Sam': 'Feb 13'}

print('my name is Alice and my birthday is ' + birthdays.get('Alice', 'soon'))

# The above will use a key and print the corresponding birthday. If the key is not in the dict, the second value is used


# The setdefault() method

# allows you to assing a value to ta key if the key is not present in the dictionary

spam = {'name': 'pookie', 'age': 5}
spam.setdefault('colour', 'black') # first argument sees if the key is present. if not present it will add the key to the dictionary with the value(2nd argument in setdefault() method)
print(spam) # will return {'name': 'pookie', 'age': 5, 'colour': 'black'}

# if key is already present in the dict, the value of the key will be returned

# character_count program

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for i in message: # program loops through eacch character in the string assigned to the variable 'message'
    count.setdefault(i, 0) # method adds each character to a dict and sets it to 0 if the key is not present 
    count[i] = count[i] + 1 # everytime a letter that is already in the dict appears, the count of that letter increases by 1
print(count) # return the final dict {' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5,
# 'd': 3, 'g': 2, 'i':6, 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}

# import pprint to make the final dict look much neater 

pprint.pprint(count) or print(pprint.pformat(count)) # will give you the dict in a much neater format 
'''
{' ': 13,
 ',': 1,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 6,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}
 '''
