# for and odd number of elements in LL, return the midddle and for even items in the LL return the second of the middel 2

# creating the Node class
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

    def print_LL(self):
        if self.head is None:
            return "empty list"
        iterate_linked_list = self.head
        ll_string = ''
        while iterate_linked_list:
            ll_string += str(iterate_linked_list.data)
            iterate_linked_list = iterate_linked_list.next
        print(ll_string)

    def get_ll_length(self):
        count = 0
        ll_index = self.head
        while ll_index:
            ll_index = ll_index.next
            count += 1
        return count

    def return_median(self):
        if self.get_ll_length() % 2 == 0:
            "Even length of ll"
        median_index = self.get_ll_length() // 2
        return median_index

    def get_ll_at_index(self, index):
        if index > self.count - 1:
            return "Index out of Bound"
        value_index = self.head
        count = 0
        while value_index:
            value_index = value_index.next
            count += 1
            if count == index:
                return value_index.data


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(9)
    ll.insert_at_beginning(8)
    ll.insert_at_beginning(7)
    ll.print_LL()
    print(ll.get_ll_length())
    print("Count is " + str(ll.count))
    print("Median is at index " + str(ll.return_median()))
    print(ll.get_ll_at_index(ll.return_median()))
