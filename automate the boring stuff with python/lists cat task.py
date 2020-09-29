catnames = []
while True:
    name = input('Enter the name of cat ' + str(len(catnames) + 1) + ' (Or enter \
nothing to stop.):')
    if name == '':
        break
    catnames = catnames + [name]
    print('The cats are called:')
    for name in catnames:
        print('' + name)
