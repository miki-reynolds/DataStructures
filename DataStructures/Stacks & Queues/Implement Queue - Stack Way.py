'''
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

e.g.

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
'''

class QueueStackWay:
    def __init__(self):
        # the reverse array i.e. the first num added at the end
        self.first = []
        # the normal array i.e. the first num added at the beginning
        self.last = []

    # push method
    def enqueue(self, x: int):
        while self.first:
            self.last.append(self.first.pop())
        
        self.last.append(x)

    # pop method
    def dequeue(self):
        while self.last:
            self.first.append(self.last.pop())
        
        num = self.first.pop()
        return num

    # access first num
    def peek(self):
        return self.last[0] if len(self.last) > 0 else self.first[-1] 

    def empty(self) -> bool:
        return not (self.first and self.last)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()