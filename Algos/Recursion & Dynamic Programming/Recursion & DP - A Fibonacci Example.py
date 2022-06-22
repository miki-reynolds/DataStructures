'''
Recursion:
Any loop problems can be done in recursion and vice versa.

https://www.geeksforgeeks.org/types-of-recursions/
- Types of recursion:
1. Direct Recursion (4 subtypes)
a. Tail Recursion
b. Head Recursion
c. Tree Recursion
d. Nested Recursion

2. Indirect Recursion
'''

'''
Criteria for Dynamic Programming solutions:
1. can be divided into sub-problems
2. recursive solutions
3. repetitive sub-problems?
4. memoize sub-problems

In Python, we can employ the FUNCTOOLS module that comes with @lru_cache to gain more insights. 
It comes wit a cache_info() where hits are good (already in cache), misses are bad (gotta calculate), ...
https://realpython.com/lru-cache-python/

Here is a SOF post on DP_Top_Down (Recursive) vs DP_Bottom_Up (Loop) when it comes to Time & Space Complexity.
https://stackoverflow.com/questions/53740511/dynamic-programming-recursionmemoization-vs-looplist
'''


# For Fibonacci Sequence and similar problems, remember to ask interviewers if they include 0 at the beginning.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233

# if curious, helper variable just to compare the plain recursive vs the dp recursive
# calculation = 0


# Non-LRU-CACHE method, we create our own Higher-Order Function/Closure
def fibonacci_dp():
    cache = {}

    def fibonacci_dp(n):
        # global calculation 
        # calculation += 1
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            cache[n] = fibonacci_dp(n-2) + fibonacci_dp(n-1)
        return cache[n]

    return fibonacci_dp


# LRU-CACHE method - the Top-Down Dynamic Programming Method

from functools import lru_cache

@lru_cache
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n-2) + fibonacci_lru(n-1)


# The Bottom-Up Dynamic Programming Method
def fibonacci_loop(n):
    result = [0, 1]
    for i in range(2, n+1):
        result.append(result[i-2] + result[i-1])
        i += 1
    return result.pop()


fib = fibonacci_dp()
print(fib(10))
print(fibonacci_lru(10))
print(fibonacci_lru.cache_info())
print(fibonacci_loop(10))

