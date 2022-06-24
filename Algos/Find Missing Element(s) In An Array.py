'''
Two cases (Sorted Array With A One Increment For Each Element)

1. Single Missing Element in An Array
a. Natural Nums (1,2,3,4,5,...)
b. Non-natural Nums (9,10,11,12,13....)

Missing_Ele = Sum of Natural Nums - Sum of Array
Missing_Ele = Index_Difference + Difference (Index & Element)

2. Multiple Missing Elements in An Array
a. Sorted Array
b. Non-Sorted Array
'''
# [1, 2, 3, 4, 5, 6, 8, 9]
#  0  1  2  3  4  5  6  7
# Single Missing Element - Natural Nums in Sorted Array
def find_single_missing_element1(array):
    length = len(array)
    if not length:
        return "Empty Array"

    sum_natural_num = (array[-1]*(array[-1]+1))/2
    missing_ele = sum_natural_num - sum(array)
    return missing_ele

# Single Missing Element in Sorted Array
def find_single_missing_element2(array):
    length = len(array)
    if not length:
        return "Empty Array"

    diff_init = array[0] - 0
    for i in range(length):
        diff_vs = array[i] - i
        if diff_vs > diff_init:
            missing_ele = i + diff_init
            break
    return missing_ele


# [1, 2, 3, 4, 8, 9]
#  0  1  2  3  4  5
# Single Multiple Elements in Sorted Array
def find_multiple_missing_elements1(array):
    length = len(array)
    if not length:
        return "Empty Array"

    missing_eles = []
    diff_init = array[0] - 0
    for i in range(length):
        diff_vs = array[i] - i
        
        if diff_init != diff_vs:
            # condition to break the iteration to find missing elements
            while diff_init < diff_vs:
                missing_ele = i + diff_init
                missing_eles.append(missing_ele)
                diff_init += 1

    return missing_eles


# Time O(n) - works for UNSORTED Array (Hashing)
def find_multiple_missing_elements2(array):
    length = len(array)
    if not length:
        return "Empty Array"

    whole_array = dict()
    missing_eles = []

    for i in range(length):
        whole_array[array[i]] = 1

    low = array[0]
    high = array[-1]
    while low <= high:
        if not whole_array.get(low):
            missing_eles.append(low)
        low += 1

    return missing_eles


if __name__ == '__main__':
    # print(find_single_missing_element1([1, 2, 3, 4, 5, 6, 8, 9]))
    # print(find_single_missing_element2([1, 2, 3, 4, 5, 6, 8, 9]))
    # print(find_multiple_missing_elements1([1, 2, 3, 4, 8, 9]))
    print(find_multiple_missing_elements2([2, 1, 3, 10, 8, 9]))
    

