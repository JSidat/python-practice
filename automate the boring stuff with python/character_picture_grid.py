grid =  [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

rows = len(grid) # gives the number of rows in the grid ie. there are 9 lists/items within the overall list
cols = len(grid[0]) # gives the number of columns in the grid/the number of items in each element in the list

# we want x to stay constant whilst y increases up till the last row in the grid
# then we want x to increase by 1, and then repeat the same process as above 
# this continues until we reach the last column

for x in range(len(grid[0])): # determines the number of times the nested for loop will run
    for y in range(len(grid)): # determines the number of iterations i.e the number of items in the list
        print(grid[y][x], end=' ') # end term stops a new line starting after each iteration
    print()
