from collections import Counter 

s = sorted(input()) # sorted function converts the string to a list of characters in alphabetical order
c = Counter(s).most_common(3) # Counter funcion will count the occurences of each character, most_common will give the top 3 
for i, j in c: # for each character and number in list, 
    print(i, j) # print character and number next to each other
