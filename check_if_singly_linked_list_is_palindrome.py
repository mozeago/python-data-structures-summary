class Node:
    def __init__(self, value, next_value=None):
        self.data = value
        self.next = next_value


# method 1
# use a stack of list nodes
# 1. traverse and push all nodes to stack
# 2. traverse again but nowfor every visited node, pop a node from the stack and compare data popped node with the
# currently visited node
# 3. if all nodes matched then return true else false
# Method 2
#

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)

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

    def check_is_palindrome(self, head: Node) -> bool:
        slow_pointer = self.head
        fast_pointer = self.head
        stack = []
        while fast_pointer and fast_pointer.next:
            stack.append(fast_pointer.data)
            print("fast pointer " + str(fast_pointer.data))
            print("Slow pointer " + str(slow_pointer.data))
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        if fast_pointer:
            slow_pointer = slow_pointer.next
        while slow_pointer and stack:
            if slow_pointer.data != stack.pop():
                return False
        return True

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
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(1)
    ll.print_linked_list()
    ll.check_is_palindrome(1)
