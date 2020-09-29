def comma(items):
    new_string = '' # empty string to store the new comma seperated words
    for item in items: # iterate through each item in the list
        new_string += str(item) # add item to the new_string variable as string values
        if items.index(item) == (len(items)-2):  # identify the penultimate item
            new_string += ', and '  # put ', and' after adding this item to the new-string variable
        elif items.index(item) == (len(items)-1): # identify the final item in the list
            new_string = new_string   # gives the final value for the variable
        else:
            new_string += ', '  # otherwise add ', ' after each item is added to the list
    return new_string  # return the final value for the variable

spam= ['apples', 'bananas', 'tofu', 'cats']
print(comma(spam))

    
