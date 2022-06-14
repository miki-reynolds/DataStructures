// Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
// For Example:
// const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
// should return false.
//-----------
// const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
// should return true.

// 2 parameters - arrays - no size limit
// return true or false


const array1 = ['a', 'b', 'c', 'x'];
const array2 = ['z', 'y', 'a'];


// brute force O(a*b) Time - Space O(1)
function containsCommonItem(arr1, arr2) {
  // empty array(s)
  if (!arr1.length || !arr2.length || (!arr1.length && !arr2.length)) {
    return false;
}
  // nonempty arrays
  for (let i=0; i < arr1.length; i++) {
    for ( let j=0; j < arr2.length; j++) {
      if(arr1[i] === arr2[j]) {
        return true;
      }
    }
  }
  return false;
}


// Better approach Time O(a + b) - Space O(a)
function containsCommonItem2(arr1, arr2) {
   // empty array(s)
   if (!arr1.length || !arr2.length || (!arr1.length && !arr2.length)) {
    return false;
  }
  // nonempty arrays
  let map = new Map();
  // create a hash table with keys being the nums in array1
  for (let i=0; i < arr1.length; i++) {
    if(!map[arr1[i]]) {
      const item = arr1[i];
      map[item] = true;
    }
  }
  // loop through array2 and check if item in exists in the hash table. 
  for (let j=0; j < arr2.length; j++) {
    if (map[arr2[j]]) {
      return true;
    }
  }
  return false;
}


// built-in method
function containsCommonItem3(arr1, arr2) {
  return arr1.some(item => arr2.includes(item))
}


console.log(
containsCommonItem(array1, array2),
containsCommonItem2(array1, array2),
containsCommonItem3(array1, array2)
)





// The some() method in JavaScript:
// checks if any array elements pass a test(provided as a callback function).
// executes the callback function once for each array element.
// returns true (and stops) if the function returns true for one of the array elements.
// returns false if the function returns false for all of the array elements.
// does not execute the function for empty array elements.
// does not change the original array.


// -----------------------------------------

// MAP vs Objects in JavaScript
// Map is a collection of keyed data items, just like an Object, which only allows string keys). But the main difference is that Map allows keys of any type.

// Methods and properties are:

// new Map() – creates the map.
// map.set(key, value) – stores the value by the key.
// map.get(key) – returns the value by the key, undefined if key doesn’t exist in map.
// map.has(key) – returns true if the key exists, false otherwise.
// map.delete(key) – removes the value by the key.
// map.clear() – removes everything from the map.
// map.size – returns the current element count.