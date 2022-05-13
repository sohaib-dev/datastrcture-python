"""Implementation of basic stack operations using list

Stack is a linear data structure, perform operations in the order of First in Last out(FILO). Usually it supports four
basic operations of push(), pop(), peek() and is_empty(). ALl four operations take same time of O(1).
Implementing stack using array saves memory as no pointers are involved, but it's not dynamic.
"""

from sys import maxsize


class Stack:
    """Implement the four basic operations of stack using list."""

    def __init__(self):
        """It will initialize the stack."""
        self.stack = list()

    def push(self, value):
        """It will add the element at the stack."""
        self.stack.append(value)
        print("The element {} pushed to the stack".format(value))

    def pop(self):
        """It will remove the element from top of stack."""
        if self.is_empty():
            return str(-maxsize-1)
        return self.stack.pop()

    def peek(self):
        """Returns the top element of stack."""
        if self.is_empty():
            return str(-maxsize - 1)
        return self.stack[-1]

    def is_empty(self):
        """Check if the element is empty or not."""
        return len(self.stack) == 0


if __name__ == '__main__':
    stack = Stack()
    stack.push(6)
    print(stack.peek())
    print(stack.pop())
    print(stack.is_empty())
