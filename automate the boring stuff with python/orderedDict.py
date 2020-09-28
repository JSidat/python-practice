from collections import * # import collection module where the OrderedDict function is
N= int(input()) # enter input for the number of items
d= OrderedDict() # create an empty dictionary 
for i in range(N): # loop through the items based on the number of items specified above
    item = input().split() # input the name of the item and the price of the item
    itemPrice= int(item[-1]) # get the item price which will be the last item after the split
    itemName= " ".join(item[:-1]) # get the itemName, this will be everything apart from the itemPrice
    if d.get(itemName):    # get() checks if the itemName has a value and if a value is present,
       d[itemName] += itemPrice  # add the value of this iteration to the value already in the dictionary 
    else:  # otherwise
       d[itemName] = itemPrice # create a new key-value pair with the new itemName and itemPrice
for i in d.keys(): # for each key in the dictionary
    print(i, d[i])  # print the key and the value corresponding to that key