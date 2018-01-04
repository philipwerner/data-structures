"""Create a deque class."""


from dll import DoubleLinkedList


class Deque(object):
    """Deque data structure, can add and remove from both ends."""

    def __init__(self):
        """Initialize the deque."""
        self.deque = DoubleLinkedList()

    def append(self, value):
        """Add an item to the back of the deque."""
        self.deque.append(value)

    def append_left(self, value):
        """Add an item to the front of the deque."""
        self.deque.push(value)

    def pop(self):
        """Pop a value off of the back of the deque and return it."""
        return self.deque.shift()

    def pop_left(self):
        """Pop a value off of the front of the deque and return it."""
        return self.deque.pop()

    def peek(self):
        """Return the next value that would be poped at the end of deque."""
        try:
            return self.deque.tail.data
        except AttributeError:
            return None

    def peek_left(self):
        """Return the next value to pop in the deque."""
        try:
            return self.deque.head.data
        except AttributeError:
            return None

    def size(self):
        """Return the number of nodes in the deque."""
        return self.deque.__len__()

