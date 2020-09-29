# Perform append, pop, popleft and appendleft methods on an empty deque 
'''
# actions used on the deque
6
append 1
append 2
append 3
appendleft 4
pop
popleft
'''

from collections import deque # import deque function from collections module 

n = int(input())  # input for the number of actions being carried out on deque
d= deque()  # create an empty deque
for i in range(n):    # for each action in range n
    command = input().split()  # input the action being carried out, but seperate the command from the number in a list
    action = command[0]  # the actual action (append, pop, popleft, appendleft) will be the first element of the list
    if len(command) > 1: # if the list is longer then 1 element, i.e. the list has an action and a number
        element = command[1] # the number will be at index 1 of the list
    if action == 'append':  # if the action is 'append':
        d.append(element) # append the number in the list to the deque
    elif action == 'pop': # if the action is 'pop':
        d.pop()   # this will remove the element to the right of the deque
    elif action == 'appendleft': # if the action is 'appendleft':
        d.appendleft(e) # this will append the number specified to the left of the deque
    elif action == 'popleft': # if the action is 'popleft':
        d.popleft() # this will remove the element to the left of the deque
print(*d) # print the deque with the unpack operator removing all the brackets to give just the numbers