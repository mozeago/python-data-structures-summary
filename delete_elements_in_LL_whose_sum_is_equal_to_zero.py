class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Given some resources in the form of linked list you have to canceled out all the resources whose sum up to 0(Zero)
# and return the remaining list.
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

    def sum_of_two_LL(self):
        slow_pointer = self.head
        prev_slow_pointer = self.head
        drag_pointer = self.head
        while slow_pointer.next is not None:
            prev_slow_pointer = slow_pointer
            slow_pointer = slow_pointer.next
            sum = int(slow_pointer.data) + int(prev_slow_pointer.data)
            if sum < 0:
                return "less than zero"
            elif sum == 0:
                print("last stop is ")
        return "End of Loop, next of slow pointer is None"


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(0)
    ll.insert_at_beginning(0)
    ll.insert_at_beginning(11)
    ll.print_linked_list()
    print(ll.sum_of_two_LL())
    ll.print_linked_list()
