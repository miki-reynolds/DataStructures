# Implementing Basic Array from Object/Dictionary/Hash Map
class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    

    def get(self, index):
        return self.data[index]
    

    def append(self, value):
        self.data[self.length] = value
        self.length += 1
        return self.length
    

    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem
    

    def delete(self, index):
        item = self.data[index]
        self.shift_items(index)
        return item
    

    def shift_items(self, index):
        for i in range(self.length):
            self.data[i] = self.data[i + 1];
        
        # delete the last item in the array because we move it up already
        del self.data[self.length - 1]
        # decrease the length of array
        self.length -= 1
    

    def unshift(self, value):
        for i in range(self.length):
            self.data[i] = self.data[i + 1]
    
        self.data[0] = value
        self.length += 1


'''
Common methods e.g. reverse, merge, insert
'''
# Check If the Array Is Sorted
def sorted_array(array):
    length = len(array)

    if not length:
        return "Empty Array"
    elif length == 1:
        return True
    else:
        for i in range(length-1):
            if array[i] > array[i+1]:
                return False
        return True


# Reverse Array Function ([::-1], reverse())
def reverse(array):
    length = len(array)
    
    if not length:
        return "Empty Array"

    # We only loop through half to avoid a 360deg swapping
    # Even if the array's length is odd, the middle number remains unchanged in position, i.e. think of horizontal symmetry.
    for i in range(length//2):
        array[i], array[-i-1] = array[-i-1], array[i]
    return array


# Insert at a position Function
def insert(array, pos, num):    
    array.append(num)
    length = len(array)

    for i in range(length-1, pos, -1):
        array[i] = array[i-1]

    array[pos] = num
    return array


# Insert A Number In A Sorted Array Function 
def insert_num(array, num):    
    array.append(array[-1]) # increase the length of array with the max number of array -> also works for the condition below
    length = len(array)
    i = length-1
    
    while array[i] > num: # stop when array[i] < num
        array[i] = array[i-1]
        i -= 1

    # insert right at array[i+1] where its value is a current dup of array[i]
    array[i+1] = num

    return array


# Shift Negative Nums To the Left & Positive Nums To the Right
def shift_negative_positive(array):
    length = len(array)

    if not length or length == 1:
        return array

    i, j = 0, length-1

    while i < j:
        if array[i] > 0 and array[j] < 0:
            array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
            
        if array[i] < 0:
            i += 1
        if array[j] > 0:
            j -= 1
    print(array)
    # return array


if __name__ == '__main__':
    # print(reverse([1, 2, 3, 4, 5]))
    # print(insert([0, 1, 2, 3, 4 ,5], 3, 6))
    # [0, 1, 2, 6, 3, 4 ,5]
    # print(insert_num([0, 1, 2, 4 ,5], 3))
    print(shift_negative_positive([0, 1, 2, -4 ,-5, 12, -13, 14]))
    

