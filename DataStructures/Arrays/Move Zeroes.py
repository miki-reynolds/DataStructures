"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


e.g.
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

e.g.
Input: nums = [0]
Output: [0]

Edge Cases:
1. Sorted? (probably not)
If sorted, use count() to count zero from top for non-negative numbers and then move the counts of zeroes to the end.
2. Always non-empty? Only 1 element?
3. Repeating nums?
"""


# Time O(n)
def move_zeroes(nums):
    length = len(nums)

    # empty array or one-element array"
    if not length:
        return "Array is empty"
    elif length == 1:
        return nums
    
    else:
        for i in range(len(nums)):
            if nums[i] == 0:
                temp = nums.pop(i)
                nums.append(temp)

        return nums


if __name__ == "__main__":
    move_zeroes([0,1,0,3,12])
