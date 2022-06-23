// loop method
function reverseString(string) {
    // check input
    if (!string || string.length < 2 || typeof string !== 'string') {
        return "Not enough characters to reverse the string!";
    }

    const backWards = [];
    len = string.length;

    for (i = len; i >= 0; i--) {
        backWards.push(string[i]);
    }
    return backWards.join("");
}


// built-in method in JavaScript
function reverseString1(string) {
    return string.split("").reverse().join("");
}


console.log(reverseString("Try this and see!"))