'''
Stacks are linear data-structures which can be implemented using either stacks or linked lists
Insertion and deletion of elements in a stack take place from one end only.
Stacks follow the LIFO rule - Last In First Out, where the last element that is inserted, is the first element that comes out.
The main operations that can be performed on a stack , with their time complexities are as follows:
Push (Insert) - O(1)
Pop (Remove) - O(1)
Peek (Retrieve the top element) - O(1)
'''


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def push(self, data):
        new_node = Node(data)
        if self.top == None: 
            self.top = new_node
            self.bottom = new_node
        else: 
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.top == None: 
            print("Stack empty")
        else: 
            self.top = self.top.next
            self.length -= 1
            if(self.length == 0):
                self.bottom = None

    def print_stack(self):
        if self.top == None:
            print("Stack empty")
        else:
            current_pointer = self.top
            while(current_pointer!=None):
                print(current_pointer.data)
                current_pointer = current_pointer.next


if __name__ == '__main__':
    my_stack = Stack()
    print(my_stack.peek())
    #None

    my_stack.push('google')
    my_stack.push('udemy')
    my_stack.push('discord')
    my_stack.print_stack()
    #discord
    #udemy
    #google

    print(my_stack.top.data)
    #discord

    print(my_stack.bottom.data)
    #gogle

    my_stack.pop()
    my_stack.print_stack()
    #udemy
    #google

    my_stack.pop()
    my_stack.pop()
    my_stack.print_stack()
    #Stack Empty
