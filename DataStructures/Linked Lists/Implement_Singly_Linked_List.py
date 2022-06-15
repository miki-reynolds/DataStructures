'''
Linked lists are, as the name suggests, a list which is linked.
It consists of nodes which contain data and a pointer to the next node in the list.
The list is connected with the help of these pointers.
These nodes are scattered in memory, quite like the buckets in a hash table.
The node where the list starts is called the head of the list and the node where it ends, or last node, is called the tail of the list.
The average time complexity of some operations involving linked lists are as follows:
Look-up : O(n)
Insert  : O(n)
Delete  : O(n)
Append  : O(1)
Prepend : O(1)
Python doesn't have a built-in implementation of linked lists, we have to build it on our own
'''

# blueprint for nodes
class Node():
    def __init__(self, data): 
        self.data = data 
        # Pointer (null/none/another node)
        self.next = None 


# Singly Linked List 
class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    # Time O(1)
    def append(self, data):
        new_node = Node(data)

        # if linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1

        # if linked list is non-empty
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    # Time O(1)
    def prepend(self, data):
        new_node = Node(data)

        # if linked list is empty
        if self.head is None:
            self.append(self, data)
        
        # if linked list is non-empty
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    # Time O(n)
    def insert(self, position, data):
        new_node = Node(data)

        # if linked list is empty OR
        # if position >= linked list's length
        if self.head is None or position >= self.length:
            self.append(data)

        elif position == 0:
            self.prepend(data)

        # otherwise, insert into the position given
        else:
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next

            # link new node (B) to the node after it (C) (A C -> A B C) -> push node C* to the next position
            new_node.next = current_node.next # *
            # link current node (A) to its next node - the new node (B)
            current_node.next = new_node
            self.length += 1
    
    # Time O(n)
    def delete_by_value(self, data):
        # if linked list is empty
        if self.head is None:
            print("There is no data in the linked list.")
            return
        # if linked list is non-empty
        
        current_node = self.head
        # if data is in head
        if current_node.data == data:
            self.head = self.head.next
            # if the new head or next node is None
            if self.head is None or self.head.next is None:
                self.tail = self.head
            self.length -= 1
            return
                
        # else, retrieve the previous node before the node that contains the data
        while current_node.next is not None and current_node.next.data != data:
            current_node = current_node.next
        
        # link the node after current_node (the prev node) to the current_node.next.next as current_node.next is the node with data
        if current_node.next is not None:
            current_node.next = current_node.next.next
            if current_node.next is None:
                self.tail == current_node
            self.length -= 1
            return
    
    # Time O(n)
    def delete_by_position(self, position):
        # if position >= linked list's length
        if position >= self.length:
            print(f"Node at {position} is non-existent!")
            return

        current_node = self.head
        # if position is at head
        if position == 0:
            self.head = self.head.next
            # if the new head or next node is None
            if self.head is None or self.head.next is None:
                self.tail = self.head
            self.length -= 1
            return
                
        # else, retrieve the prev node before the node in question
        for i in range(position - 1):
            current_node = current_node.next
        
        # bypass the node in question and link the prev node to the node after the node in question
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next is None:
            self.tail = current_node
        return

    # Time O(n)
    def print_list(self):
        current_node = self.head
        if current_node is None:
            print("Empty linked list")
            return

        while current_node is not None:
            print(current_node.data, end =" ")
            current_node = current_node.next
        print()


#We will import this file while reversing a linked list. So we must make sure that it runs only
#when it is the main file being run and not also when it is being imported in some other file.
if __name__ == '__main__':

    my_linked_list = SinglyLinkedList()
    my_linked_list.print_list()
#Empty

    my_linked_list.append(5)
    my_linked_list.append(2)
    my_linked_list.append(9)
    my_linked_list.print_list()
#5 2 9

    my_linked_list.prepend(4)
    my_linked_list.print_list()
#4 5 2 9

    my_linked_list.insert(2,7)
    my_linked_list.print_list()
#4 5 7 2 9

    my_linked_list.insert(0,0)
    my_linked_list.insert(6,0)
    my_linked_list.insert(9,3)
    my_linked_list.print_list()
#This position is not available. Inserting at the end of the list
#0 4 5 7 2 9 0 3

    my_linked_list.delete_by_value(3)
    my_linked_list.print_list()
# #0 4 5 7 2 9 0

    my_linked_list.delete_by_value(0)
    my_linked_list.print_list()
# #4 5 7 2 9 0

    my_linked_list.delete_by_position(3)
    my_linked_list.print_list()
# #4 5 7 9 0

    my_linked_list.delete_by_position(0)
    my_linked_list.print_list()
# #5 7 9 0

    my_linked_list.delete_by_position(8)
    my_linked_list.print_list()
# #5 7 9
    print(my_linked_list.length)
# #3