"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
e.g.
Input: nums = [1,2,3,1]
Output: true

e.g.
Input: nums = [1,2,3,4]
Output: false

e.g.
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

# loop method - O(n) Time - O(1) Space
def contains_duplicate1(array):
    dict = {}

    for i in range(len(array)):
        if array[i] in dict:
            return True

        dict[array[i]] = i
    
    return False
        

# "set" method - a short method in Python
# we only need to return boolean value, no key-value pair
def contains_duplicate2(array):
    return len(array) != len(set(array))


if __name__ == "__main__":
    print(contains_duplicate1([1,2,3,4]))
    print(contains_duplicate1([1,2,3,1])) 
    print(contains_duplicate2([1,2,3,4])) 
    print(contains_duplicate2([1,2,3,1])) 
