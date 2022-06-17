# loop method
def reverse_string(str):
    reverse_str = ""
    for i in range(len(str) - 1, -1, -1):
        reverse_str += str[i]
        
    return reverse_str


# built-in slicing method in Python
def reverse_string1(str):
    return str[::-1]
    # return "".join(reversed(str))


# another native method (sort of)
def reverse_string2(str):
    return "".join(reversed(str))


if __name__ == "__main__":
    print(reverse_string("Try this and see!"))
    print(reverse_string1("Try this and see!"))
    print(reverse_string2("Try this and see!"))


"""
COMMON & USEFUL STRINGS METHODS IN PYTHON
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