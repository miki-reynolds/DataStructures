array = ['a','b','c','d']
# 4*4 = 16 bytes of storage is used

print(array[2])

#push  
array.append('e')          # O(1)
#pop  
array.pop() 
array.pop()                # O(1)

#add first element 
array.insert(0,'x')        #O(n)

#splice
array.insert(2,'alien')    #O(n)

print(array)


"""
COMMON & USEFUL ARRAY METHODS IN PYTHON

append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes and returns the element at the specified index
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

List objects are implemented as arrays. 
They are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) 
operations which change both the size and position of the underlying data representation.

For in depth information on arrays 
https://docs.python.org/3/tutorial/datastructures.html

to implement arrays as a stack 
https://docs.python.org/3/library/collections.html#collections.deque
"""


"""
COMMON & USEFUL STRING METHODS IN PYTHON
capitalize()	Converts the first character to upper case
upper()	        Converts a string into upper case
lower()	        Converts a string into lower case
isupper()	    Returns True if all characters in the string are upper case
islower()	    Returns True if all characters in the string are lower case

swapcase()	    Swaps cases, lower case becomes upper case and vice versa

join()	        Converts the elements of an iterable into a string
split()	        Splits the string at the specified separator, and returns a list
strip()	        Returns a trimmed version of the string
count()	        Returns the number of times a specified value occurs in a string
startswith()	Returns true if the string starts with the specified value
endswith()	    Returns true if the string ends with the specified value
find()	        Searches the string for a specified value and returns the position of where it was found
index()	        Searches the string for a specified value and returns the position of where it was found

isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isascii()	    Returns True if all characters in the string are ascii characters
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isnumeric()	    Returns True if all characters in the string are numeric
isspace()	Returns True if all characters in the string are whitespaces
"""