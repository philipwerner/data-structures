"""Node module."""


class Node(object):
    """The node object."""

    def __init__(self, value, next=None):
        """Build node attributes on init."""
        self.value = value
        self.next = next
