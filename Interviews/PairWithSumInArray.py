# # Google Interview Question Example
# "https://www.youtube.com/watch?v=XKu_SEDAykw&t=897s&ab_channel=LifeatGoogle"


'''
Two Sum Problem
Given an array, find a pair within the array whose sum is equal to the number provided.
e.g.
arr1 = [1, 2, 3, 4] and sum = 4
-> True, arr1[0] + arr1[2] = 4
[5, 9, 12, 15] and sum = 100
-> False
'''

'''
Brainstorming Edge Cases:
1. Empty Array?
2. Ordered/Unordered?
3. All numbers?
4. Repeated numbers?
4. Negative/Floating?
'''


# brute force O(n^2)
def hasPairWithSum(arr, sum):
    length = len(arr)
    i = 0

    while i < length:
        j = i + 1
        while j < length:
            if arr[i] + arr[j] == sum:
                return True
            j += 1
        i += 1

    return False


# Better O(n)
def hasPairWithSum2(arr, sum):
    mySet = set()
    len = len(arr)
    i = 0

    while i < len:
        if arr[i] in mySet:
            return True
        mySet.add(sum - arr[i])
        i += 1 
    return False


# Sets in Python
# https://www.programiz.com/python-programming/set