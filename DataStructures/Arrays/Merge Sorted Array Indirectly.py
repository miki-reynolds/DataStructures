"""
This problem doesn't modify any array directly and return a new array. The length of each array only holds enough elements in itself.
"""


# Time O(n1 + n2 + ) & Space O(n1 + n2) 
def merge_sorted_arrays(arr1, arr2, n1, n2):
    arr3 = [None] * (n1 + n2)
    i, j, k = 0, 0, 0

    # Traverse both arrays
    # Check if current element of first array is smaller than current element of second array. If yes, store first array element and increment first array index. Otherwise do same with second array
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr3[k] = arr2[j]
            k += 1
            j += 1
     
    # Store remaining elements of first array
    while i < n1:
        arr3[k] = arr1[i]
        k += 1
        j += 1
 
    # Store remaining elements of second array
    while j < n2:
        arr3[k] = arr2[j]
        k += 1
        j += 1

    return arr3
