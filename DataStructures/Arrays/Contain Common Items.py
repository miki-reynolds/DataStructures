'''
Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items, 
e.g.
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']
should return false.

e.g.
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x'];
should return true.

2 parameters - arrays - no size limit and return values should be True or False
'''


array1 = ['a', 'b', 'c', 'x'];
array2 = ['z', 'y', 'a'];


# brute force
# or more accurately Time Complexity O(a*b) and Space Complexity O(1)
def containsCommonItem(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)

    # in case no elements in arr1 and/or arr2
    if len1 == 0 or len2 == 0 or (len1 == 0 and len2 == 0):
        return False

    # in case no empty arrays
    for i in range(len2):
        for j in range(len2):
            if arr1[i] == arr2[j]:
                return True
    
    return False


# Better approach
# O(a + b) Time Complexity and Space Complexity O(a)
def containsCommonItem2(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)

    # empty array(s)
    if len1 == 0 or len2 == 0 or (len1 == 0 and len2 == 0):
        return False

    # nonempty arrays
    dict1 = {arr1[i]: "{arr1[i]}" for i in arr1}
    
    for j in range(len(arr2)):
        if arr2[j] in dict1:
            return True
    
    return False


