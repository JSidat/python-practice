from math import inf
from collections import deque

n = int(input()).strip() 

for i in range(n):
    x = int(input().strip()) # strip method removes spaces from the beginning and end of a string
    d = deque(map(int, input().split(' '))) # for each value inputted in the deque, convert it to an int type 
    test = True
    current_value = inf # sets the current value to infinity(infinitely long floor)

    while d: # loop through d
        le = d[0] # left element  is at index 0
        re = d[-1] # right element is at index -1

        if le >= re and current_value >= le: # if left element greater then right element and smaller then current floor value
            current_value = d.popleft() # make the top of the pile the left most value
        elif re >= le and current_value >= re: # if the right value greater then the left value and top of the pile is greater then or equal to the right value
            current_value = d.pop() # make the top of the list the right most value
        else: # otherwise
            test = False # piling cant occur, set flag to False
            break

    if test:  # if the flag is True at the end of the loop,
        print('Yes') # print 'Yes'
    else: # otherwise
        print('No') # print 'No'

