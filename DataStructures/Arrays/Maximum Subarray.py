"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

e.g.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

e.g.
Input: nums = [1]
Output: 1

e.g.
Input: nums = [5,4,-1,7,8]
Output: 23
"""


# One property of DP problem is the subproblem property, once we solve the subproblem, we can solve the whole problem. The only thing we need to do is find the transition from subproblem to the big problem. Since each subarray must have a end, lets say we now have the maximum subarray ends at n-1, we want to get the maximum subarray ends at n, the transitionn is obvious, if maximum sum of subarray ends at n-1 is negative, the maximum subarray ends at n equals to its own value, since any number add negative number will be smaller. if instead it it positive, the maximum subarray ends at n euqals to its own value plus the maximum subarray ends at n-1. For the base case, when there is only one element in the array, the maximum is easy to compute.


# Time O(n)
def max_subarray(nums):
    # assuming nonempty array (obviously double-check)
    # array only has 1 num
    if len(nums) == 1:
        return nums[0]
        
    # otherwise
    sum_result = [0 for i in range(len(nums))]
    sum_result[0] = nums[0]

    for i in range(1,len(nums)):
        if sum_result[i-1] < 0:
            sum_result[i] = nums[i]
        else:
            sum_result[i] = sum_result[i-1] + nums[i]
        
        print(sum_result)

    return max(sum_result)


if __name__ == "__main__":
    print(max_subarray([5,4,-1,7,8]))
    print(max_subarray([4,-1,2,1]))
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
