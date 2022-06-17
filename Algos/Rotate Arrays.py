"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

e.g. 
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

e.g.
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


*Please remember to (always) ask: 
"Are we allowed to use built-in methods from the language?"

Ege Cases:
1. Always non-empty? Always numeric (doesn't really matter)?
2. k is bigger than the array's length?
Still want the array to be rotated or no?
If yes, (k-length) will be the new k to rotate.
3. k = array's length? -> stays the same
4. Rotation in place?
"""


# built-in concat method in Python 
# Time O(a+b)
def rotate_array(arr, k):
    length = len(arr)
    # empty array or k = array's length
    if not length or length == 1 or length == k:
        return arr
    
    # non-empty array
    else:
        k = k % length
        arr[:] = arr[-k:] + arr[:-k]
        return arr


if __name__ == "__main__":
    print(rotate_array([1,2,3,4,5,6,7], 3))
