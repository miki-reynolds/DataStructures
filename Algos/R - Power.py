'''
If there is a formula, it's better to use it to save time and space. Recursion is costly because it consumes call stack.
We can also use iteration.
'''

# Time O(n)
def power(base, n):
    if base == 0:
        return base
    elif n == 0:
        return 1
    else:
        for i in range(2, n):
            base *= base
        return base


# Easier-To-Read Method: Incorporation of Recursion & DP
# We can create a a decorator function ourselves.

from functools import lru_cache

@lru_cache
def power_recursive_dp(base, n):
    if base == 0:
        return base
    elif n == 0:
        return 1
    else:
        return power_recursive_dp(base, n-1)*base


# Best Method e.g. (2^2)^4 = 2^8
@lru_cache
def power_recursive_best(base, n):
    if base == 0:
        return base
    elif n == 0:
        return 1
    else:
        if n % 2 == 0:
            return power_recursive_best(base*base, n/2)
        else:
            return base*power_recursive_best(base*base, (n-1)/2)


if __name__ == '__main__':
    print(power(4, 4))
    print(power_recursive_dp(4, 4))
    print(power_recursive_best(4, 4))