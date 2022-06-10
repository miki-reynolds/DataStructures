// Google Interview Question Example
// https://www.youtube.com/watch?v=XKu_SEDAykw&t=897s&ab_channel=LifeatGoogle



// Pair With Sum Problem
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



// brute force O(n^2)
function hasPairWithSum(arr, sum){
  var len = arr.length;
  for(var i =0; i<len-1; i++){
     for(var j = i+1;j<len; j++){
        if (arr[i] + arr[j] === sum)
            return true;
     }
  }
  return false;
}


// Better O(n)
function hasPairWithSum2(arr, sum){
  const mySet = new Set();
  const len = arr.length;
  for (let i = 0; i < len; i++){
    if (mySet.has(arr[i])) {
      return true;
    }
    mySet.add(sum - arr[i]);
  }
  return false;
}


hasPairWithSum2([6,4,3,2,1,7], 9)
