# Time & Max Space O(n^2)
def bubble_sort(array):
    length = len(array)
    flag = 0 # make BB sort more efficient by initiating flag
    if not array or length == 1:
        return array

    for i in range(length-1):
        flag = 0
        # range(length-1-i) because when one "i" comparisons have already been done in their turn
        for j in range(length-1-i):
            if array[j] > array[j + 1]:
                # swap
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = 1

        if not flag: #no sorting happens because array is already sorted
            break

    return array


if __name__ == '__main__':
    print(bubble_sort([3, 4, 8, 1, 2, 9]))

