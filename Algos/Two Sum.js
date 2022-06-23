// Two Sum Problem
// Given an array, find a pair within the array whose sum is equal to the number provided.
// e.g.
// arr1 = [1, 2, 3, 4] and sum = 4
// -> True, arr1[0] + arr1[2] = 4
// [5, 9, 12, 15] and sum = 100
// -> False

// Brainstorming Edge Cases:
// 1. Empty Array?
// 2. Ordered/Unordered?
// 3. All numbers?
// 4. Repeated numbers?
// 4. Negative/Floating?


// brute force Time O(n^2)
function twoSum(arr, sum){
  var len = arr.length;
  for(var i =0; i<len-1; i++){
     for(var j = i+1;j<len; j++){
        if (arr[i] + arr[j] === sum)
            return true;
     }
  }
  return false;
}


// "hash table" method - Time O(n) 
function twoSum1(arr, sum){
  const mySet = new Set();
  const len = arr.length;
  const remaining = sum - arr[i];

  for (let i = 0; i < len; i++){
    if (mySet.has(arr[i])) {
      return true;
    }
    mySet.add(remaining);
  }
  return false;
}

// other hash table methods
// could implement another function using object but it's a pain with keys only being strings in JS. 
// another way is to do new Map()


twoSum([6,4,3,2,1,7], 9)
twoSum1([6,4,3,2,1,7], 9)
