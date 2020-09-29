def even_fib_sum(limit=10):
    fn_2, fn_1, fn = 1, 1, 0
    even_sum = 0
    while fn < limit:
        fn_2, fn_1, fn = fn_1, fn, fn_1 + fn_2
        if fn%2 == 0:
            even_sum += fn
    return even_sum

print(even_fib_sum())