# Reverse Array Function
def reverse(array):
    length = len(array)
    
    if not length:
        return "Empty Array"

    # We only loop through half to avoid a 360deg swapping
    # Even if the array's length is odd, the middle number remains unchanged in position, i.e. think of horizontal symmetry.
    for i in range(length//2):
        array[i], array[-i-1] = array[-i-1], array[i]
    return array


if __name__ == '__main__':
    print(reverse([1, 2, 3, 4, 5]))