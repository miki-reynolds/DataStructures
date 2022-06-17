"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array **should not** be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

e.g.
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

e.g.
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

e.g.
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""


# built-in method in Python - a cheating method
def merge_sorted_arrays0(nums1, nums2, m, n):
    nums1[:] = sorted(nums1[:m] + nums2[:n])


# Time O(a + b) - Space O(1)
def merge_sorted_arrays1(nums1, m, nums2, n):
        last, i, j = m + n - 1, m - 1, n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                last, i = last - 1, i - 1
            else:
                nums1[last] = nums2[j]
                last, j = last - 1, j - 1

        # circle back to get the current possible remaining elements at the start of nums2 to replace the head(s) of nums1
        while j >= 0:
                nums1[last] = nums2[j]
                last, j = last - 1, j - 1

        return nums1    


if __name__ == "__main__":
    arr1 = [3, 5, 7, 8, 0, 0, 0, 0]
    n1 = len(arr1)
    
    arr2 = [1, 2, 4, 6]
    n2 = len(arr2)
    print(merge_sorted_arrays1(arr1, n1-n2, arr2, n2))
 

# to understand better how this works
# [3, 5, 7, 8, 0, 0, 0, 0]
# [1, 2, 4, 6]
# 1st loop - num 1:  8
# 1st loop - num 2:  6
# [3, 5, 7, 8, 0, 0, 0, 8]

# [3, 5, 7, 8, 0, 0, 0, 8]
# [1, 2, 4, 6]
# 1st loop - num 1:  7
# 1st loop - num 2:  6
# [3, 5, 7, 8, 0, 0, 7, 8]

# [3, 5, 7, 8, 0, 6, 7, 8]
# [1, 2, 4, 6]
# 1st loop - num 1:  5
# 1st loop - num 2:  6
# [3, 5, 7, 8, 0, 6, 7, 8]

# [3, 5, 7, 8, 0, 6, 7, 8]
# [1, 2, 4, 6]
# 1st loop - num 1:  5
# 1st loop - num 2:  4
# [3, 5, 7, 8, 5, 6, 7, 8]

# [3, 5, 7, 4, 5, 6, 7, 8]
# [1, 2, 4, 6]
# 1st loop - num 1:  3
# 1st loop - num 2:  4
# [3, 5, 7, 4, 5, 6, 7, 8]

# [3, 5, 7, 4, 5, 6, 7, 8]
# [1, 2, 4, 6]
# 1st loop - num 1:  3
# 1st loop - num 2:  2
# [3, 5, 3, 4, 5, 6, 7, 8]

# [3, 5, 3, 4, 5, 6, 7, 8]
# [1, 2, 4, 6]
# 2nd loop - num 1:  5 with last =  1
# 2nd loop - num 2:  2 with j =  1
# [3, 2, 3, 4, 5, 6, 7, 8]

# [3, 2, 3, 4, 5, 6, 7, 8]
# [1, 2, 4, 6]
# 2nd loop - num 1:  3 with last =  0
# 2nd loop - num 2:  1 with j =  0
# [1, 2, 3, 4, 5, 6, 7, 8]