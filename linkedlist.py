class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


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

    def insert_at_the_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            # we return here to void having 41-->41-->14. ie double execution of statements
            return
        iterate_linked_list = self.head
        while iterate_linked_list.next:
            iterate_linked_list = iterate_linked_list.next
        # when we have reached the LL tail
        iterate_linked_list.next = Node(data)


if __name__ == '__main__':
    linked_list = LinkedList()
    # linked_list.insert_at_beginning(45)
    # linked_list.insert_at_beginning(5)
    # linked_list.insert_at_beginning(4)
    linked_list.insert_at_the_end(41)
    linked_list.insert_at_the_end(14)
    linked_list.insert_at_the_end(24)
    linked_list.insert_at_the_end(34)

    linked_list.print_linked_list()
