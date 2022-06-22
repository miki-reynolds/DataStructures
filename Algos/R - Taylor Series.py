'''
If there is a formula, it's better to use it to save time and space. Recursion is costly because it consumes call stack.
We can also use iteration.

The Taylor Series e^x is a combination of multiple values like sum, power and factorial term, hence we will use static variables.

For the power of x, we will use p, and for factorials, we will use f as static variables. 
'''

# Loop Method - Better Time Complexity
def taylor_series(x, n):
    sum = 1
    for i in range(n, 0, -1):
        sum = 1 + (x/i)*sum
    return sum


# Same Method in Recursion
sum = 1
def taylor_series_recursive(x, n):
    global sum
    if n == 0:
        return sum
    sum = 1 + (x/n)*sum
    return taylor_series_recursive(x, n-1)


# DP-Recursive Method
from functools import lru_cache

p, f = 1, 1 
@lru_cache
def taylor_series_recursive_dp(x, n):
    if x == 0:
        return False
    # Termination condition
    elif (n == 0):
        return 1
    else:
        global p, f
        # Recursive call
        r = taylor_series_recursive_dp(x, n - 1)
    
        # Update the power of x
        p = p * x
        # Factorial
        f = f * n
        return (r + p / f)



if __name__ == '__main__':
    print(taylor_series(4, 15))
    print(taylor_series_recursive(4, 15))
    print(taylor_series_recursive_dp(4, 15))
    # 54.597883



# ---------------------------------------------------------------- #
'''
"nonlocal" means that a variable is "neither local or global", i.e, the variable is from an enclosing namespace (typically from an outer function of a nested function).

An important difference between nonlocal and global is that the a nonlocal variable must have been already bound in the enclosing namespace (otherwise an syntaxError will be raised) while a global declaration in a local scope does not require the variable is pre-bound (it will create a new binding in the global namespace if the variable is not pre-bound).
'''
