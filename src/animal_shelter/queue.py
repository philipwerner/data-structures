"""Queue module."""
from node import Node


class Queue(object):
    """Queue class that uses first in first out principle."""

    def __init__(self, iterable=None):
        """."""
        self.front = None
        self.rear = None
        if isinstance(iterable, (tuple, list)):
                for item in iterable:
                    self.insert(item)

    def enqueue(self, val):
        """Add a node to the end of the queue."""
        to_add = Node(val)
        if self.front is None:
            self.front = to_add
            self.rear = to_add
            return val
        else:
            temp = self.rear
            temp.next = to_add
            self.rear = to_add
            return val

    def dequeue(self):
        """Remove and return the front of the Queue."""
        if self.front is None:
            raise ValueError("Queue is Empty")
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value

    def peek(self):
        """Show the value at the front of the queueu."""
        if self.front is None:
            raise ValueError("Queue is empty")
        else:
            return self.front.value
