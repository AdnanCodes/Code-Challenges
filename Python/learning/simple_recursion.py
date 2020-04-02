# Simple summation of a given integer

# 4 -> 4+3+2+1 = 10
# 3 -> 3 + 2 + 1 = 6


def iterative_sum_integer(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum


print('Iterative solution: ', iterative_sum_integer(2))


def recursive_sum_integer(n):
    if n == 0:
        return 0
    else:
        return recursive_sum_integer(n-1) + n


print('Recursive Solution: ', recursive_sum_integer(3))
