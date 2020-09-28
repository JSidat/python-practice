from collections import OrderedDict              #
dict = OrderedDict()  # create ordered dictionary to store the word as a key and occurences as values

for i in range(int(input())):  # get an input for the number of words                                     
    key = input()   # input the amount of words specified in the line above
    if not key in dict.keys():    # if the word is not in the dictionary as a key
        dict.update({key : 1}) # update the dictionary by adding the word and increase the count/ value by 1
        continue  # continue back to the top of the loop
    dict[key] += 1 # if the word/key is in the dictionary, increase the value of the key by 1

print(len(dict.keys())) # print the amount of keys to give the number of unique words
print(*dict.values()) # print the values of the keys to give the number of occurences
                      # * is used as an unpack operator to get the values from odict_values([2, 1, 1]) to 2, 1, 1  
                        