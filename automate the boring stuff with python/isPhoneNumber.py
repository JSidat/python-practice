def isphonenumber(text):
    if len(text) != 11:
           return False
    for i in range(0, 1):
        if not text[i].isdecimal():
            return False
    if text [0] != '0' and text[1] != '7':
        return False
    return True

print('07124859648 is a phone number:')
print(isphonenumber('07124859648'))
print('09187375638992 is a phone number:')
print(isphonenumber('09187375638992'))
