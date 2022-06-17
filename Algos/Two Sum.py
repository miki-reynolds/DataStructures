# # Google Interview Question Example
# "https://www.youtube.com/watch?v=XKu_SEDAykw&t=897s&ab_channel=LifeatGoogle"


'''
Two target Problem
Given an array, find a pair within the array whose target is equal to the number provided.
e.g.
arr1 = [1, 2, 3, 4] and target = 4
-> True, arr1[0] + arr1[2] = 4
[5, 9, 12, 15] and target = 100
-> False

Edge Cases:
1. Empty Array?
2. Ordered/Unordered?
3. All numbers?
4. Repeated numbers?
4. Negative/Floating?
'''


# brute force O(n^2)
def two_sum0(arr, target):
    length = len(arr)
    i = 0

    while i < length:
        j = i + 1
        while j < length:
            if arr[i] + arr[j] == target:
                return True
            j += 1
        i += 1

    return False


# "set" method - Better Time O(n) 
def two_sum1(arr, target):
    my_set = set()
    length = len(arr)
    i = 0

    while i < length:
        if arr[i] in my_set:
            return True
        my_set.add(target - arr[i])
        i += 1 
    return False


# "hash table" method - Better Time O(n) 
def two_sum2(arr, target):
    seen = {}

    for i in range(len(arr)):
        remaining = target - arr[i]
        if arr[i] in seen:
            return True
        seen[remaining] = remaining
    
    return False


if __name__ == "__main__":
    print(
        two_sum2([5, 7, 9, 12], 12), two_sum2([5, 7, 9, 13], 13))



# Sets in Python
# https://www.programiz.com/python-programming/set