def sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum


def power(x, n):
    prod = 1
    for i in range(1, n + 1):
        prod = prod * x
    return prod
