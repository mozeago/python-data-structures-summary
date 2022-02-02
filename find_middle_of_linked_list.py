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
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(9)
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(7)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(10)
    ll.print_LL()
    print("Count is " + str(ll.count))
    print(ll.get_median())
