class BinarySearchTreeNode:
    def __init__(self, data):
        self.node = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.node:
            return
        if data < self.node:
            # insert to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # insert to right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.node)
        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.node
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.node
        return self.left.find_min()


def build_tree(elements):
    root_node = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root_node.add_child(elements[i])
    return root_node


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18]
    tree = build_tree(numbers)
    print(tree.inorder_traversal())
