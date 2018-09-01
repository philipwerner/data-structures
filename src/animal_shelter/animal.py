"""Animal class module."""


class Animal(object):
    """Animal class."""

    def __init__(self, value, next=None):
        """Build node attributes on init."""
        self.value = value
        self.next = next
