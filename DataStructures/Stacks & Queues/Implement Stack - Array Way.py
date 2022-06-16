'''
Stacks can be implemented with the help of arrays as well.
We can insert and delete elements only at the end of the array(the top of the stack)
Python comes built-in with lists which are basically arrays.
They contain functionalities like append and pop which correspond to the push and pop methods of stacks respectively
So implementing stacks using arrays is pretty simple in Python
The time complexities of different operations are same as that for the inked list implementation of stacks
'''


class Stack():
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array)-1]

    def push(self, data):
        self.array.append(data)
        return

    def pop(self):
        if len(self.array)!= 0:
            self.array.pop()
            return
        else:
            print("Stack Empty")
            return

#Stack follows LIFO, so for the print operation, we have to print the last element of the list first.
#This will require a loop traversing the entire array, so the complexity is O(n)
    def print_stack(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i])
        return


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push("Miki")
    my_stack.push("Is")
    my_stack.push("A")
    my_stack.push("SDE!")
    my_stack.print_stack()
   
    my_stack.pop()
    my_stack.pop()
    my_stack.print_stack()

    print(my_stack.peek())

    print(my_stack.__dict__)



'''
Stacks can be implemented in Python in two more ways.    1. Using the 'deque' class from 'collections' module. Same methods used in lists, append and pop are used in deque.
2. Using 'LifoQueue' from the 'queue' module . 'put()' and 'get()' methods are used for pushing and popping. It comes with some other useful methods async well. 
'''