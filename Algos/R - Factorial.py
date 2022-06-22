'''
If there is a formula, it's better to use it to save time and space. Recursion is costly because it consumes call stack.
We can also use iteration.
'''

# Time O(n)
def factorial(num):
    if num <=1:
        return num

    facto = 1
    for i in range(1, num+1):
        facto *= i
    return facto


# Easier-To-Read Method: Incorporation of Recursion & DP
# We can create a a decorator function ourselves.

from functools import lru_cache

@lru_cache
def factorial_recursive_dp(num):
    if num <= 2:
        return num
    
    return factorial_recursive_dp(num-1)*num



if __name__ == '__main__':
    print(factorial(4))
    print(factorial_recursive_dp(4))
