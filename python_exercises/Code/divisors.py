def divisors(num):
    divisor_list =[]
    for number in range(1, num):
        if num % number == 0:
            divisor_list.append(number)
    return divisor_list


