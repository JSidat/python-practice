 #Given two strings a and b, return the characters that are not common in the two strings.


def solve(a,b):
    new_string = ''
    for i in a:
        if i in b:
            continue
        new_string += i
    for i in b:
        if i in a:
            continue
        new_string += i
    return new_string