'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
e.g.
Input: root = [2,1,3]
Output: true

e.g.
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

# blueprints for BST
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # InOrder Traversal (We get sorted order of elements in tree)
    def print_tree(self):
        if self.root is not None:
            self.printt(self.root)

    def printt(self, current_node):
        if current_node:
            self.printt(current_node.left)
            print(str(current_node.data))
            self.printt(current_node.right)

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            # looping till find where to insert appropriately
            while True:
                # left is less (smaller values)
                if data < current_node.data:
                    # insert where left has not been established
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    # increment current node to the next left
                    current_node = current_node.left
                # otherwise, go to the right; right is more (bigger values)
                else:
                    # insert where right has not been established
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    # increment current node to the next right
                    else:
                        current_node = current_node.right

    # InOrder (Sorted):
    # Draw an arrow down and draw along the outline of the tree from left to right (Prof Abdul)
    def dfs_traverse_in_oder(self, node, result):
        if node is None:
            return result
        # print("Start ", node.data, end=" ")

        if node.left:
            self.dfs_traverse_in_oder(node.left, result)
        # print()
        # print(result)
        result.append(node.data)

        if node.right:
            self.dfs_traverse_in_oder(node.right, result)

        return result

    # validating bst mean we basically need to see if elements from left to right are sorted ascendingly
    # hence, an inorder DFS is needed
    # Time O(n) Space O(h) - tree height
    def validate_bst(self):
        if self.root is None:
            return True

        current_node = self.root
        result = []
        self.dfs_traverse_in_oder(current_node, result)

        for i in range(len(result) - 1):
            if result[i] > result[i+1]:
                return False

        return True


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(4)
    bst.insert(6)
    bst.insert(20)
    bst.insert(90)
    bst.insert(15)
    bst.insert(1)
    # bst.print_tree()

    x = bst.validate_bst()
    print(x)
