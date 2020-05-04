# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡­ The numbers after the direction are steps. 
# Please write a program to compute the distance from current position after a sequence of movement and original point. 
# If the distance is a float, then just print the nearest integer. 
# Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 
# Then, the output of the program should be: 2

import math

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



    
    
