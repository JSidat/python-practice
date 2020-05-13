#Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
#we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the 
#successive powers of p is equal to k * n.


def dig_pow(n, p):
    total = 0
    for num in str(n):
        total += int(num) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1