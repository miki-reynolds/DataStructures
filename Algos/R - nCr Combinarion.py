'''
If there is a formula, it's better to use it to save time and space. Recursion is costly because it consumes call stack.
We can also use iteration.

The Combination Formula is nCr = n!/[r!(n-r)!].
r <= n; r can't be bigger than n.
e.g. We have A B C D E F G
Select  ABC, ABD, ACB (nope, this is not nPr; we need new selection).
'''


from functools import lru_cache

# helper function for factorials
@lru_cache
def factorial_recursive_dp(num):
    if num <= 2:
        return num
    
    return factorial_recursive_dp(num-1)*num

# DP-Recursive Method
@lru_cache
def combination_recursive(n, r):
    facto_n = factorial_recursive_dp(n)
    facto_r = factorial_recursive_dp(r)
    facto_nr = factorial_recursive_dp(n-r)

    return facto_n/(facto_r*facto_nr)


# Pascal-DP-Recursive Method
@lru_cache
def combination_recursive_pascal(n, r):
    if r == 0 or n == r:
        return 1
    return combination_recursive(n-1, r-1) + combination_recursive(n-1, r)


if __name__ == '__main__':
    print(combination_recursive(4, 15))
    print(combination_recursive(4, 15))



