#multiplies all the elements in a list

def product(numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total
print(product([2, 4, 2]))
