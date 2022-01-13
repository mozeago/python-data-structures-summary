class Node:
    def __init__(self, data):
        self.node_data = data
        self.next_node = None
        self.prev_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node

    def print_linked_list(self):
        iterate_ll = self.head

        while iterate_ll:
            print(iterate_ll.node_data)
            iterate_ll = iterate_ll.next_node


doublyll = LinkedList()
doublyll.insert_at_beginning(3)
doublyll.insert_at_beginning(4)
doublyll.insert_at_beginning(7)
doublyll.print_linked_list()
