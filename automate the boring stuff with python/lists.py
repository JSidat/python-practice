# lists can contain other lists

spam = [['bat', 'cat'], 'wolf', 'elephant', 'camel']

print(spam[0]) # returns the first list in the list

print(spam[0][1]) # first index decides which list to use, second number indicates the value within that list

print(spam[-1]) # prints the last item in the list

# getting sublists with slices
# a slice translates to a new list

spam = ['cat', 'dog', 'pig', 'elephant']

print(spam[1:3]) # prints the items at index 1 and 2, value in the second index not included

print(spam[:3]) # prints the items from the beginning when no number is specified before the colon

print(spam[1:]) # prints the list starting at index 1, to the end of the list

# length of list

print(len(spam)) # prints the number of items in the list

# changing values in the list using indexes

spam[1] = 'Rabbit' # replaces the item at index 1 with the new word specified

print(spam)

# list concatenation and list replication

print([1, 1, 2, 3] + ['hello', 'what' 'how']) # joins the two strings together to make one long string

print(spam * 3) # print the list 3 times as one long list

# removing values from a list

del(spam[2]) # removes the item at index 2 in the list
print(spam)

# working with lists

catNames = []
while True:
    print('Enter the name of the cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cats names are: ')
for name in catNames:
    print(name)

# using loops with lists
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# in and not in operators
# used to determine whether an item is or not in a list

myPets = ['Betsy', 'Dave', 'Tommmy', 'Bastian']
name = (input('Enter name here: '))
if name not in myPets:
    print('I dont have any pets with that name')
else:
    print('Yes that is my pet!')

# multiple assignment trick
# the values in a list canbe assigned to variables as follows:

cat = ['fat', 'black', 'loud']
size = cat[0]
colour = cat[1]
desposition = [2]

# the above can also be written as:

cat = ['fat', 'black', 'loud']
size, colour, desposition = cat # number of variables and the length of the list must be equal 

# Methods

# finding a value in a list using the index method

spam = ['hello', 'bye', 'howdy', 'Heyas']
spam.index('hello') # will return the index of hello i.e. 0
spam.index('howdy') # will return the index of howdy i.e. 2

# if duplicates are present the inex of the first occurence will be returned

# Adding values to lists using the append() and insert() methods

spam = ['hello', 'bye', 'howdy', 'Heyas']
spam.append('see ya') # adds see ya to the end of the list

spam = ['hello', 'bye', 'howdy', 'Heyas']
spam.insert(1, 'inabit') # adds inabit to index 1 in the list

# removing items from lists using remove()

spam = ['hello', 'bye', 'howdy', 'Heyas']
spam.remove('hello') # removes hello from the list

# sorting the values in a list using the sort() method

spam = ['hello', 'bye', 'howdy', 'Heyas']
spam.sort() # sorts the list out in alphabetical order
spam.sort(reverse=True) # sorts the item in the list in reverse order


# list-like data types

# strings can be considered a list of characters

name = 'sophie'
print(name[0]) # will print the first character in the name
print(name[-2]) # will print the second to last character in the name
print(name[1:4]) # will print 'oph' 

for i in name:
    print('***' + i + '***') # will return * * * Z * * *
                             #             * * * o * * *
                             #             * * * p * * *
                             #             * * * h * * *
                             #             * * * i * * *
                             #             * * * e * * *

# muttable and immutable data types

# converting types with the list() and tuple() functions

spam = ['hello', 'bye', 'howdy', 'Heyas']
print(tuple(['hello', 'bye', 'howdy', 'Heyas'])) # will return the items in a tuple i.e. ('hello', 'bye', 'howdy', 'heyas')

list(('cat', 'dog', 'rabbit')) # will return the tuple values as a list i.e. ['cat', 'dog', 'rabbit']

# converting a tuple to a list could be useful if you want to make changes to the tuple




