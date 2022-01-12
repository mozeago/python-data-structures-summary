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

    def delete_at_index(self, index):
        if index < 0 or index >= self.get_linked_list_length():
            raise Exception("Invalid index")
            return

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        iterate_linked_list = self.head
        while iterate_linked_list:
            if count == index - 1:
                iterate_linked_list.next = iterate_linked_list.next.next
                break
            count += 1
            iterate_linked_list = iterate_linked_list.next

    def get_linked_list_length(self):
        count = 0
        iterate_linked_list = self.head
        while iterate_linked_list:
            iterate_linked_list = iterate_linked_list.next
            count += 1

        return count

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_linked_list_length():
            raise Exception("Invalid index to insert at")
            return
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        iterate_linked_list = self.head
        while iterate_linked_list:
            if count == index - 1:
                new_node = Node(data, iterate_linked_list.next)
                iterate_linked_list.next = new_node
                break
            iterate_linked_list = iterate_linked_list.next
            count += 1

    def delete_at_beginning(self):
        self.head = self.head.next
        return

    def delete_at_end(self):
        count = 0
        iterate_linked_list = self.head
        while iterate_linked_list:
            if count == self.get_linked_list_length() - 2:
                iterate_linked_list.next = None
                return
            iterate_linked_list = iterate_linked_list.next
            count += 1


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_beginning(45)
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_beginning(4)
    linked_list.print_linked_list()
    # linked_list.insert_at_the_end(41)
    # linked_list.insert_at_the_end(14)
    # linked_list.insert_at_the_end(24)
    # linked_list.insert_at_the_end(34)
    # print("Length is:----->" + str(linked_list.get_linked_list_length()))
    # linked_list.delete_at_index(3)
    #linked_list.insert_at_index(1, 9)
    #linked_list.print_linked_list()
    #linked_list.insert_at_index(3, 37)
    # linked_list.delete_at_beginning()
    linked_list.delete_at_end()
    linked_list.print_linked_list()
    print("head is:---->" + str(linked_list.head.data))
