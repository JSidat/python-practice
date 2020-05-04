import inflect
p = inflect.engine()

def number_to_words(n):
    return p.number_to_words(n)

word = number_to_words(923341573943234)
print(word)