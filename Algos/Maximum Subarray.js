// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
// A subarray is a contiguous part of an array.

// e.g.
// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.

// e.g.
// Input: nums = [1]
// Output: 1

// e.g.
// Input: nums = [5,4,-1,7,8]
// Output: 23


// Time O(n) - Space O(1)
// JavaScript has +- Infinity but Python does not.
function maxSubarray0(nums) {
    let currSum = -Infinity;
    let maxSum = -Infinity;
    for(let i = 0; i < nums.length; i++) {
        currSum = Math.max(0, currSum);
        currSum += nums[i];
        maxSum = Math.max(maxSum, currSum);
    }
    return maxSum;
}


// Time O(n) - Space O(1)
function maxSubarray(array) {
    let sumArray = new Array(array.length).fill(0);
    sumArray[0] = array[0];

    for (let i = 1; i < array.length; i++) {
        if (sumArray[i - 1] < 0) {
            sumArray[i] = array[i];
            console.log(sumArray);
        }
        else {
            sumArray[i] = sumArray[i - 1] + array[i];
            console.log(sumArray);
        }    
    }
    return Math.max(...sumArray);
}


console.log(maxSubarray([5,4,-1,7,8]))







