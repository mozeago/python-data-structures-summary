# for and odd number of elements in LL, return the midddle and for even items in the LL return the second of the middel 2

# creating the Node class
import math


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)
        self.count += 1

    def get_median(self):
        slow_pointer = self.head
        fast_pointer = self.head
        prev_slow_pointer = self.head
        while fast_pointer != None and fast_pointer.next != None:
            prev_slow_pointer = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        if fast_pointer:
            return slow_pointer.data
        else:
            return (slow_pointer.data + prev_slow_pointer.data) / 2

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


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(9)
    ll.insert_at_beginning(8)
    ll.insert_at_beginning(7)
    ll.insert_at_beginning(6)
    print("Count is " + str(ll.count))
    print(ll.get_median())
