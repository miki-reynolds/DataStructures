'''
If there is a formula, it's better to use it to save time and space. Recursion is costly because it consumes call stack.
In this case, the formula is (n(n+1))/2.
We can also use iteration.
'''

# Time O(n)
def sum_of_natural_nums(num):
    i = 0
    sum = 0
    for i in range(num+1):
        sum += i
        i += 1
    return sum


# Time & Space O(n)
def sum_of_natural_nums_recursive(num):
    sum = 0
    if num == 0:
        return sum
    return sum_of_natural_nums_recursive(num-1) + num


# Better Method: Incorporation of Recursion & DP
# We can create a a decorator function ourselves.

from functools import lru_cache

@lru_cache
def sum_of_natural_nums_recursive_dp(num):
    sum = 0
    if num == 0:
        return sum
    return sum_of_natural_nums_recursive(num-1) + num

if __name__ == '__main__':
    print(sum_of_natural_nums(5))
    print(sum_of_natural_nums_recursive(5))
    print(sum_of_natural_nums_recursive_dp(5))