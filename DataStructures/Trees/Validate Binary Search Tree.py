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

def validate_bst(node):
    if node.root is None:
        return True

    current_node = node.root
    count = 0
    result = []

    while current_node:
        if current_node.left:
            if current_node.data >= current_node.left:
                result.append("True")
            else:
                result.append("False")
            current_node = current_node.left

        if current_node.right:
            if current_node.data <= current_node.right:
                result.append("True")
            else:
                result.append("False")
            current_node = current_node.right
        
    if "False" in result:
        return False
    
    return True


class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

# Returns true if given tree is BST.
def validate_bst_recursive(root, left=None, right=None):
	if (root == None) :
		return True

	if (left != None and root.data <= left.data) :
		return False

	if (right != None and root.data >= right.data) :
		return False

	# check recursively for every node.
	return validate_bst_recursive(root.left, left, root) and validate_bst_recursive(root.right, root, right)


if __name__ == '__main__':
	root = Node(3)
	root.left = Node(2)
	root.right = Node(5)
	root.right.left = Node(1)
	root.right.right = Node(4)
	#root.right.left.left = newNode(40)
	if (isBST(root,None,None)):
		print("Is BST")
	else:
		print("Not a BST")


    