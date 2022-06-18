# blueprints for BST
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Inorder Traversal (We get sorted order of elements in tree)
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

    def lookup(self, data):
        if self.root is None:
            return False

        current_node = self.root
        while current_node:
            if data == current_node.data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            elif data > current_node.data:
                current_node = current_node.right

        return False

    def remove(self, data):
        if not self.root:
            return False

        parent_node = None
        current_node = self.root

        while current_node:
            # left is less
            if data < current_node.data:
                parent_node = current_node
                current_node = current_node.left
            # right is more
            elif data > current_node.data:
                parent_node = current_node
                current_node = current_node.right
            # match found
            else:
                # case1: no right child
                if current_node.right is None:
                    # match found at main branch
                    if parent_node is None:
                        self.root = current_node.left
                    # match found passed main branches
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                        else:
                            parent_node.right = current_node.left

                # case2: right child (of the current node) with no left child
                elif current_node.right.left is None:
                    current_node.right.left = current_node.left
                    # match found at main branch
                    if parent_node is None:
                        self.root = current_node.right
                    # match found passed main branches
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                        else:
                            parent_node.right = current_node.right

                # case3: right child with both left and right child nodes
                # https://visualgo.net/en/bst - example
                # leftmost leaf of the right child is ideal
                if current_node.left and current_node.right:
                    left_most = current_node.right.left
                    left_most_parent = current_node.right

                    # Loop to reach the leftmost node of the right subtree of the current node
                    while left_most.left:
                        left_most_parent = left_most
                        left_most = left_most.left

                    # Parent's left subtree is now leftmost's right subtree
                    # leftmostParent.left = leftmost.right
                    # leftmost.left = currentNode.left
                    # leftmost.right = currentNode.right
                    if parent_node is None:
                        self.root = left_most
                    # If it has a right subtree, we simply link it to the parent of the del_node
                    else:
                        if current_node.data < parent_node.data:
                            parent_node.left = left_most
                        else:
                            parent_node.right = left_most

        return True

    def breadth_first_search(self):
        current_node = self.root
        result = []
        queue = [current_node]

        while len(queue) > 0:
            current_node = queue[0]
            queue.pop(0)
            result.append(current_node.data)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result

    def breadth_first_search_recursive(self, queue, result):
        if not len(queue):
            return result

        current_node = queue.pop(0)
        result.append(current_node.data)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        return self.breadth_first_search_recursive(queue, result)

    # InOrder (Sorted):
    # Draw an arrow down and draw along the outline of the tree from left to right (Prof Abdul)
    def dfs_traverse_in_oder(self, node, result):
        if node is None:
            return result
        print("Start ",node.data, end=" ")

        if node.left:
            self.dfs_traverse_in_oder(node.left, result)
        print()
        print(result)
        result.append(node.data)

        if node.right:
            self.dfs_traverse_in_oder(node.right, result)

        return result

    # PreOrder (L-R - Tree Copy):
    # Draw an arrow to the left and draw along the outline of the tree from left to right (Prof Abdul)
    def dfs_traverse_pre_oder(self, node, result):
        if node is None:
            return result

        result.append(node.data)
        if node.left:
            self.dfs_traverse_pre_oder(node.left, result)
        if node.right:
            self.dfs_traverse_pre_oder(node.right, result)

        return result

    # PostOrder (Bottom-up):
    # Draw an arrow to the right and draw along the outline of the tree from left to right (Prof Abdul)
    def dfs_traverse_post_oder(self, node, result):
        if node is None:
            return result

        if node.left:
            self.dfs_traverse_post_oder(node.left, result)
        if node.right:
            self.dfs_traverse_post_oder(node.right, result)
        result.append(node.data)

        return result

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(4)
    bst.insert(6)
    bst.insert(20)
    bst.insert(90)
    bst.insert(15)
    bst.insert(1)
    x = bst.lookup(6)
    print(x)
    y = bst.lookup(99)
    print(y)
    # bst.print_tree()
    # print(bst.breadth_first_search_recursive([bst.root], []))
    print(bst.dfs_traverse_in_oder(bst.root, []))
    # print(bst.dfs_traverse_pre_oder(bst.root, []))
    # print(bst.dfs_traverse_post_oder(bst.root, []))