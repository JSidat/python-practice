def even_digits(x, y):

    new_list = []
    for a in range(x, y + 1):
        if all(int(b) % 2 == 0 for b in str(a)):
            new_list.append(a)
    return new_list

print(even_digits(1000, 3001))
