// You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

// Merge nums1 and nums2 into a single array sorted in non-decreasing order.

// The final sorted array **should not** be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

// e.g.
// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
// Output: [1,2,2,3,5,6]
// Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
// The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

// e.g.
// Input: nums1 = [1], m = 1, nums2 = [], n = 0
// Output: [1]
// Explanation: The arrays we are merging are [1] and [].
// The result of the merge is [1].

// e.g.
// Input: nums1 = [0], m = 0, nums2 = [1], n = 1
// Output: [1]
// Explanation: The arrays we are merging are [] and [1].
// The result of the merge is [1].
// Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


// built-in method
// function mergeSortedArrays(arr1, m, arr2, n)
//     arr1.concat(arr2).sort((a,b) => (a - b))


function mergeSortedArrays(arr1, m, arr2, n) {
    m--;
    n--;
    let last = arr1.length - 1;

    while (last >= 0) {
      if (n >= 0 && m >= 0 && arr1[m] >= arr2[n]) {
        arr1[last] = arr1[m];
        arr1[m] = arr2[n];
        m--;
      }
      else if (n >= 0) {
          arr1[last] = arr2[n];
          n--;
      }
      last--;
    }
    return arr1
  };


arr1 = [3, 5, 7, 8, 0, 0, 0, 0]
arr2 = [1, 2, 4, 6]
n = arr2.length
console.log(mergeSortedArrays(arr1, 4, arr2, n))

