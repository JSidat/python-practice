s = input()
dict = {}
for i in s:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
        sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

print(sorted_dict)


#
#list(sorted_dict.items())[:3])
