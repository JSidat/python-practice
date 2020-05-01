def times_table(x):
    final_list = []
    y=1
    while y < 11:
        final_list.append(x * y)
        y += 1
    return final_list

print(times_table(8))

