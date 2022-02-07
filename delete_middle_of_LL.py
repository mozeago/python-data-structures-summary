class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Delete Middle of Linked List
# Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.
# If there are even nodes, then there would be two middle nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.
# If the input linked list is NULL or has 1 node, then it should return NULL
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

    def get_middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head
        prev_slow_pointer = self.head
        prev_node = self.head
        while fast_pointer != None and fast_pointer.next != None:
            prev_slow_pointer = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        if fast_pointer:
            prev_slow_pointer.next = slow_pointer.next
            return slow_pointer.data
        else:
            prev_slow_pointer.next = slow_pointer.next
            return slow_pointer.data


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(7)
    ll.insert_at_beginning(9)
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(76)
    ll.print_linked_list()
    print(ll.get_middle_node())
    ll.print_linked_list()
