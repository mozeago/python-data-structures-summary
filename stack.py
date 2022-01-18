from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        return self.container.append(val)

    def peek(self):
        return self.container[-1]

    def pop(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0


if __name__ == "__main__":
    mystack = Stack()
    mystack.push(2)
    mystack.push(3)
    mystack.push(5)
    mystack.push(8)
    print( mystack.peek())

