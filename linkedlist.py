class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def print_linked_list(self):
        if self.head is None:
            print("Empty Linked List")
        # get the starting point of the LinkedList
        iterate_linked_list = self.head
        linked_list_string = ''
        while iterate_linked_list:
            linked_list_string += str(iterate_linked_list.data) + '-->'
            iterate_linked_list = iterate_linked_list.next
        print(linked_list_string)


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_beginning(45)
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_beginning(4)
    linked_list.print_linked_list()
