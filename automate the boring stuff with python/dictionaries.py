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





