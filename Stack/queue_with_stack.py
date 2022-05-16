"""Implement Queue by using stack.

Queue support the First in First out(FIFO) operations. Use stack to implement the queue. deQueue() will implement the
pop() operation but enQueue() holds the logic of how stack will act as queue.
"""

from stack_linkedlist import Stack


class QueueWithStack(Stack):

    def __init__(self):
        super().__init__()
        self._fo_stack = Stack()

    def enQueue(self, data):
        """Two stack will be used. First all the elements of actual stack will be popped and pushed to the _fo_stack.
        When actual stack will be empty, a new element will be pushed as a last element. Then push all elements of
        _fo_stack back to actual stack."""
        _data = super().pop()
        while _data:
            if self._fo_stack.head:
                self._fo_stack.push(data=_data)
            else:
                self._fo_stack.push(data=_data)
            _data = super().pop()

        super().push(data)

        if self._fo_stack.head:
            _data = self._fo_stack.pop()
            while _data:
                super().push(_data)
                _data = self._fo_stack.pop()

    def deQueue(self):
        """Remove and return the element of stack"""
        return super().pop()


if __name__ == '__main__':
    queue_stack = QueueWithStack()
    queue_stack.enQueue(4)
    print(queue_stack)
    queue_stack.enQueue(5)
    print(queue_stack)
    queue_stack.enQueue(6)
    print(queue_stack)
    print(queue_stack.deQueue())
    print(queue_stack)
