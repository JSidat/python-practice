import random

def five(x, y):
    new_list = []
    for i in range(5):
        i = random.randrange(x, y+1, 2)
        new_list.append(i)
    return new_list

print(five(100, 200))
    

