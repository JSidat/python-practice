birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    name = input('Enter a name: (blank to quit)\n')
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information on ' + name)
        print('What is their birthday?')
        bday = input('Enter birthday here: ')
        birthdays[name] = bday
        print('Birthday database updated')

        
