import math
x = 0
y = 0
vertical = int(input('Enter integer here: '))
horizontal = int(input('Enter integer here: '))

if vertical > 0:
    print('UP', vertical)
elif vertical < 0:
    print('DOWN', vertical)
else:
    print('invalid entry')

if horizontal > 0:
    print('RIGHT', horizontal)
elif horizontal < 0:
    print('LEFT', horizontal)
else:
    print('invalid entry')
x = horizontal
y = vertical

print('x:',x,'y:',y)

position = math.sqrt((x**2) + (y**2))

print(int(position))



    
    