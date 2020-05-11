def odd_or_even(lst):
    new_lst= []
    for number in lst:
        if number < 5:
            new_lst.append(number)
    return new_lst


print(odd_or_even([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))
