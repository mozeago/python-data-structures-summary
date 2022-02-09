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

    def check_is_palindrome(head):
        stack_head = head
        stack_str = []
        is_palindrome = True
        while stack_head != None:
            stack_str.append(stack_head.data)
            stack_head = stack_head.next
        while head != None:
            top_of_stack = stack_str.pop()
            if top_of_stack == head.data:
                is_palindrome = True
            else:
                is_palindrome = False
                break
            head = head.next
        return is_palindrome

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
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.print_linked_list()
    ll.check_is_palindrome()
