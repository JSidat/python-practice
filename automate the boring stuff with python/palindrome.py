from collections import deque
def palindrome(word):
    new_string = ''
    d = deque()
    for letter in word:
        d.appendleft(letter)
    for i in d:
        new_string += i
    if new_string == word:
        return('This is a palindrome')
    elif new_string != word:
        return('This is not a palindrome')

print(palindrome('hello'))

