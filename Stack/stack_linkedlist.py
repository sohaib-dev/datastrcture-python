"""Implementation of basic stack operations using linked-list

Stack is a linear data structure, perform operations in the order of First in Last out(FILO). Usually it supports four
basic operations of push(), pop(), peek() and is_empty(). ALl four operations take same time of O(1).
Implementing stack using linked-list can grow and shrink dynamically, but it's not memory efficient.
"""

from sys import maxsize


class StackNode:
    """It will build a node object for stack."""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    """Implement the four basic operations of stack using linked-list."""

    def __init__(self):
        """It will initialize the head of linked-list for stack."""
        self.head = None

    def push(self, data):
        """It will add the node at the stack."""
        if self.head is None:
            self.head = StackNode(data=data)
            print("The element {} is pushed on stack.".format(data))
            return

        temp_node = self.head
        while temp_node.next_node:
            temp_node = temp_node.next_node

        temp_node.next_node = StackNode(data=data)
        print("The element {} is pushed on stack.".format(data))

    def pop(self):
        """It will remove the node from top of stack."""
        if self.is_empty():
            return str(-maxsize - 1)
        temp_node = self.head
        if temp_node.next_node is None:
            last_node = temp_node
            self.head = None
            return last_node.data
        while temp_node.next_node:
            if temp_node.next_node.next_node is None:
                last_node = temp_node.next_node
                temp_node.next_node = None
                break
            temp_node = temp_node.next_node
        return last_node.data

    def peek(self):
        """Returns the top element of stack."""
        if self.is_empty():
            return str(-maxsize - 1)
        temp_node = self.head
        if temp_node.next_node is None:
            last_node = temp_node
            return last_node.data
        while temp_node.next_node:
            if temp_node.next_node.next_node is None:
                last_node = temp_node.next_node
                break
            temp_node = temp_node.next_node
        return last_node.data

    def is_empty(self):
        """Check if the stack is empty or not."""
        if self.head is None:
            return True
        return False

    def print_stack(self):
        """Print the stack"""
        if self.head is None:
            print("stack is empty.")
            return

        list_iterator = self.head
        list_str = ''

        while list_iterator:
            list_str += str(list_iterator.data) + ' --> '
            list_iterator = list_iterator.next_node
        print(list_str)


if __name__ == '__main__':
    stack = Stack()
    print(stack.pop())
    print(stack.is_empty())
    stack.push(6)
    print(stack.pop())
    print(stack.is_empty())
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.print_stack()
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    stack.print_stack()

