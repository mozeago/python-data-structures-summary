class Node:
    def __init__(self, value, next_value):
        self.data = value
        self.next = next_value


# method 1
# use a stack of list nodes
# 1. traverse and push all nodes to stack
# 2. traverse again but nowfor every visited node, pop a node from the stack and compare data popped node with the
# currently visited node
# 3. if all nodes matched then return true else false

class LinkedList:
    def __init__(self):
        self.head = None
