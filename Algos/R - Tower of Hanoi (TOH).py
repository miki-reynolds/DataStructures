'''
If there is a formula, it's better to use it to save time and space. Recursion is costly because it consumes call stack.
We can also use iteration.

- Tower Of Hanoi (TOH):
Blocks are initially in Tower A in an ascending order (smallest on top, biggest at the bottom); but we want to move them all to Tower C. We can only move each block at a time and the bigger blocks can't be on top of the smaller ones. 
'''


# Easier-To-Read Method: Incorporation of Recursion & DP
# We can create a a decorator function ourselves, but we're going to implement LRU-Cache

# A, B, C are like blocks that we need to use to move e.g. each block from one col to the next. Initially, we employ A - from, B - auxillary, and C - to.


from functools import lru_cache

@lru_cache
def tower_of_hanoi(num, a, b, c):
    if num > 0:
        tower_of_hanoi(num-1, a, c, b)
        print(f"Moving from {a} to {c}")
        tower_of_hanoi(num-1, b, a, c)


if __name__ == '__main__':
    print(tower_of_hanoi(3, 'A', 'B', 'C'))
