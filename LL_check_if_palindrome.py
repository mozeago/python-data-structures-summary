class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


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

    def get_LL_Middle(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data

    def reverse_ll_iterative(self, head):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        #
        return prev

    def check_palindrome(self):
        ll_head = self.head
        stack_strings = []
        while ll_head:
            stack_strings.append(ll_head.data)
            ll_head = ll_head.next
        ll_head = self.head
        while ll_head:
            data_copmare = stack_strings.pop()
            if data_copmare != ll_head.data:
                return False
            ll_head = ll_head.next
        return True


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_beginning("m")
    linked_list.insert_at_beginning("a")
    linked_list.insert_at_beginning("d")
    linked_list.insert_at_beginning("a")
    linked_list.insert_at_beginning("m")
    linked_list.print_linked_list()
    print(linked_list.check_palindrome())
    # linked_list.reverse_ll_iterative(linked_list.get_LL_Middle())
    # print(linked_list.get_LL_Middle())
    # linked_list.print_linked_list()
