'''
Given a linked list we have to create a function to reverse it.
If the list is empty or consists of 1 item only we return the list as it is.
Otherwise, we create two nodes first and second which point to the first and second nodes of the list respectively
Then we update the tail of the list to point to the head as after reversing the present head will become the last node
Then we run a loop until second becomes None
Inside the loop we create a temporary node which points to the 'next' of the second node
Then we update the 'next' of the second node to point to the first node so that the link is now reversed (2nd node points to 1st node instead of 3rd).
And then we will update the first and second nodes to be equal to the second and temporary nodes respectively.
What this does is, in the next iteration, 'second' will point to the 3rd node and 'first' to the 2nd
And the 'second.next = first' statement will make the 3rd node point to the 2nd node instead of the 4th.
And this will go on till 'second' becomes None and by then all the links will be reversed.
Finally, we will update the 'next' of the head(which is still the original head) point to None as it is effectively the last node
And then we will update the head to be equal to 'first', which by now points to the last node of the original list, and return the now reversed linked list
Time complexity pretty clearly will be O(n)
'''

from Implement_Singly_Linked_List import SinglyLinkedList


def reverse(linked_list):
    if linked_list.length <=1:
        return linked_list

    # first (head) will end up being the tail
    # first and second will be exchanged in place in loops
    first = linked_list.head
    second = first.next
    linked_list.tail = linked_list.head

    while second:
        temp = second.next
        second.next = first
        first = second
        second = temp
    # set head.next to None as head now will soo be tail
    linked_list.head.next = None
    # set official head to be first, which is tail now after being swapped in loop
    linked_list.head = first
    
    return linked_list


#Now we create a Linked List by appending some values
my_linked_list = SinglyLinkedList()
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.print_list()

#2 3 4 5 6
reversed_linked_list = reverse(my_linked_list)
reversed_linked_list.print_list()
#6 5 4 3 2