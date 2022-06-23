// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.


// e.g.
// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]

// e.g.
// Input: nums = [0]
// Output: [0]


function moveZeroes(nums) {
    // check input (~ py ver.)

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            delete nums[i];
            nums.push(0);
        }
    }
    console.log(nums);
    return nums;
}

moveZeroes([0, 1, 0, 3, 12]);

