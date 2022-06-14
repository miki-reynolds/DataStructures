# Implementing Basic Array from Object


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

