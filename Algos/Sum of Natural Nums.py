'''
If there is a formula, it's better to use it to save time and space. Recursion is costly because it uses stack internally.
In this case, (n(n+1))/2.
We can also use iteration.
'''

# Time & Space O(n)
def sum_of_natural_nums_recursive(num):
    sum = 0
    if num == 0:
        return sum
    return sum_of_natural_nums_recursive(num-1) + num


# Time O(n)
def sum_of_natural_nums(num):
    i = 0
    sum = 0
    for i in range(num+1):
        sum += i
        i += 1

    return sum

print(sum_of_natural_nums(3))