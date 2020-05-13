#   create a function that removes all the vowels from a string


def disemvowel(string):
    vowels = 'AEIOUaeiou'
    new_string = ''
    for letter in string:
        if letter not in vowels:
            new_string = new_string + letter
    return new_string

    