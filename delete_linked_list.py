class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

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


    def delete_linked_list(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(6)
    ll.insert_at_beginning(7)
    ll.insert_at_beginning(9)
    print("Values are ")
    ll.print_linked_list()
    ll.delete_linked_list()
