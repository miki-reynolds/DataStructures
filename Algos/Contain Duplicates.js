// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
// e.g.
// Input: nums = [1,2,3,1]
// Output: true

// e.g.
// Input: nums = [1,2,3,4]
// Output: false

// e.g.
// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true


// loop method - O(n) Time - O(1) Space
function containsDuplicates1(array) {
    map = new Map();

    for (let i = 0; i < array.length; i++) {
        if (array[i] in map) {
            return true;
        }
        
        map[array[i]] = i;
    }
    return false;
}


// "set" method and "size" property - a short method in JavaScript
// we only need to return boolean value, no key-value pair
function containsDuplicates2(array) {
    const set = new Set(array);

    return array.length !== set.size;
}


console.log(containsDuplicates1([1, 2, 3, 1]));
console.log(containsDuplicates1([1, 2, 3, 4]));
console.log(containsDuplicates2([1, 2, 3, 1]));
console.log(containsDuplicates2([1, 2, 3, 4]));


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