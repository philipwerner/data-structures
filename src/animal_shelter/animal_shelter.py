"""AnimalShelter class."""
from animal import Animal


class AnimalShelter(object):
    """AnimalShelter base class."""

    def __init__(self, iterable=None):
        """."""
        self.front = None
        self.rear = None
        self._counter = 0
        if isinstance(iterable, (tuple, list)):
                for item in iterable:
                    self.insert(item)

    def __len__(self):
        """Return the length of the Queue."""
        return self._counter

    def enqueue(self, val):
        """Add a node to the end of the queue."""
        to_add = Animal(val)
        if self.front is None:
            self.front = to_add
            self.rear = to_add
            self._counter += 1
            return val
        else:
            temp = self.rear
            temp.next = to_add
            self.rear = to_add
            self._counter += 1
            return val

    def dequeue(self, input=None):
        """Remove and return the front of the Queue."""
        if self.front is None:
            raise ValueError("Queue is Empty")
        elif input is not None:
            found = False
            curr = self.front
            while found is False:
                if curr.value == input:
                    temp = curr.next
                    curr.next = temp.next
                    temp.next = None
                    found = True
                    self._counter -= 1
                    return temp.value
                elif curr != input:
                    curr = curr.next
                elif curr.next is None:
                    raise ValueError("No animal of that type in the shelter")
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            self._counter -= 1
            return temp.value

    def peek(self):
        """Show the value at the front of the queueu."""
        if self.front is None:
            raise ValueError("Queue is empty")
        else:
            return self.front.value
