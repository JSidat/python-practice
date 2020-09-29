# Return the string that is between the first and last appearance of "happy" in the given string

# 'welcomehappywelcome
# 'happywelcomehappy
# 'yyyhappywelcomehappyyyy

word = input("Enter word here: ")  # allow input of word
test = input('Enter another word:')  # enter the word to test against
count = word.count(test) # count the number of occurences of the word in the string inputted above 
if count <= 1:  # if the word occurs just once, 
    print(test + ' only occurs once') # print 'word only occurs once'
else:   # otherwise if the word occurs more than once
    first = word.find(test) + 5 # get the index of the first letter of the word after the input word
    end = word.find(test, first) # and get the index of the first letter of the second occurence of the input
    final = word[first:end] # slice the word in between the two occurences of the input word 
    print(final) # print the word in between the two occurences of the input word



