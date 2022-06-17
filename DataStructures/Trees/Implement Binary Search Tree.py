# blueprints for BST
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.nums_of_nodes = 0

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            self.nums_of_nodes += 1
        
        else:
            current_node = self.root

            # looping till find where to insert appropriately
            while current_node:
                # left is less (smaller values)
                if value < current_node.data:
                    # insert where left has not been established
                    if current_node.left is None:
                        current_node.left = new_node
                    # increment current node to the next left
                    else:
                        current_node = current_node.left

                # otherwise, go to the right; right is more (bigger values)
                else:
                    # insert where right has not been established
                    if current_node.right is None:
                        current_node.right = new_node
                    # increment current node to the next right
                    else: 
                        current_node = current_node.right

            self.nums_of_nodes += 1

    def lookup(self, value):
        # if not nums_of_nodes/nums_of_nodes == 0:
        if self.root is None:
            return False
        
        current_node = self.root
        while current_node:
            if value == current_node.data:
                return current_node
            elif value < current_node.data:
                current_node = current_node.left
                return current_node
            elif value > current_node.data:
                current_node = current_node.right
                return current_node
            else:
                return "Not found!"

    def remove(self, value):
        if not self.nums_of_nodes:
            return f"{value} nonexistent!"
        
        parent_node = None
        current_node = self.root

        while current_node:
            # left is less
            if value < current_node.data:
                parent_node = current_node
                current_node = current_node.left

            # right is more
            elif value > current_node.data:
                parent_node = current_node
                current_node = current_node.right

            # match found -> 4 cases
            else: 
                # case1: current_node with only left child node
                if current_node.right is None:
                    # match found at main branch
                    if parent_node is None:
                        self.root = current_node.left
                        self.nums_of_nodes -= 1
                    # match found passed main branches
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                            self.nums_of_nodes -= 1
                        else:
                            parent_node.right = current_node.left
                            self.nums_of_nodes -= 1

                # case2: current_node with only right child node
                elif current_node.left is None:
                    # match found at main branch
                    if parent_node is None:
                        self.root = current_node.right
                        self.nums_of_nodes -= 1
                    # match found passed main branches
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                            self.nums_of_nodes -= 1
                        else:
                            parent_node.right = current_node.right
                            self.nums_of_nodes -= 1

                # case3: current_node with no left and right child nodes
                elif not (current_node.left and current_node.right):
                    # match found at root
                    if parent_node is None:
                        self.root = None 
                        self.nums_of_nodes -= 1
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = None
                            self.nums_of_nodes -= 1
                        else:
                            parent_node.right = None
                            self.nums_of_nodes -= 1

                # case4: current_node with both left and right child nodes
                # https://visualgo.net/en/bst - example
                # right node of the leftmost is ideal
                if current_node.left and current_node.right:
                    # for the right subtree of the current node
                    left_most = current_node.right
                    left_most_parent = current_node.right

                    # Loop to reach the leftmost node of the right subtree of the current node
                    while left_most.left:
                        left_most_parent = left_most
                        left_most = left_most.left
                    # The value to be replaced is copied
                    current_node.data = left_most.data
                    # If the node to be deleted is the exact right child of the current node
                    if left_most == left_most_parent:
                        current_node.right = left_most.right
                    # If the leftmost node of the right subtree of the current node has no right subtree
                    elif left_most.right is None:
                        left_most_parent.left = None
                    #If it has a right subtree, we simply link it to the parent of the del_node
                    elif left_most.right:
                        left_most_parent.left = left_most.right
                    else:
                        return "Not found!"

if __name__ == '__main__':
    my_bst = BinarySearchTree()
    my_bst.insert(5)
    my_bst.insert(3)
    my_bst.insert(7)
    my_bst.insert(1)
    my_bst.insert(13)
    my_bst.insert(65)
    my_bst.insert(0)
    my_bst.insert(10)
    '''
                5
            3       7
        1               13
    0                10     65
    '''

    (my_bst.remove(13))
    '''
                5
            3       7
        1               65
    0                10     
    '''
    my_bst.remove(5)
    '''
                7
            3       65
        1        10     
    0                
    '''
    my_bst.remove(3)
    '''
                7
            1       65
        0        10                     
    '''
    my_bst.remove(7)
    '''
                10
            1       65
        0                
    '''
    my_bst.remove(1)
    '''
                10
            0       65

    '''
    my_bst.remove(0)
    '''
                10
                    65

    '''
    my_bst.remove(10)
    '''
               65


    '''
    my_bst.remove(65)
    '''


    '''

    my_bst.insert(10)
    '''
            10
    '''
    print(my_bst.root.data)
    #10

    print(123)