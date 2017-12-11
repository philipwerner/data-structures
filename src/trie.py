"""Trie module for trie tree."""


class Node:
    """Node for trie tree."""

    def __init__(self, label=None, data=None):
        """Attr upon initialization."""
        self.label = label
        self.data = data
        self.children = dict()

    def _add_child(self, key, data=None):
        """."""
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key

    def __getitem__(self, key):
        """."""
        return self.children[key]


class Trie:
    """Trie tree class."""

    def __init__(self):
        """Attr upon initialization."""
        self.root = {}
        self.head = Node()
        self._size = 0

    def __getitem__(self, key):
        """."""
        return self.head.children[key]

    def insert(self, string):
        """Insert a word to the trie tree."""
        if string is None or string == '':
            raise ValueError('A string would be nice')
        else:
            curr_node = self.head
            end_word = True
            for i in range(len(string)):
                if string[i] in curr_node.children:
                    curr_node = curr_node.children[string[i]]
                else:
                    end_word = False
                    break
            if not end_word:
                while i < len(string):
                    curr_node._add_child(string[i])
                    curr_node = curr_node.children[string[i]]
                    i += 1
            curr_node.data = string
            curr_node._add_child('$')
            self._size += 1

    def contains(self, string):
        """Check to see if trie contains a specific string."""
        if string == '':
            return ValueError('A string is required')
        if string is None:
            return ValueError('A string is required')
        curr_node = self.head
        exists = True
        for i in string:
            if i in curr_node.children:
                curr_node = curr_node.children[i]
            else:
                exists = False
                break
        if exists:
            if curr_node.data is None:
                exists = False

        return exists

    def size(self):
        """Return the total number of words in the Trie."""
        return self._size

    def remove(self, string):
        """Remove string from Trie tree."""
        if self.contains(string):
            self._size -= 1
            temp = self.root
            temp_str = list(string)
            for i in range(len(string)):
                for letter in temp_str:
                    if temp[letter] in ({'$': '$'}, {}):
                        del temp[letter]
                        temp_str.pop()
                    else:
                        temp = temp[letter]
                temp = self.root
        else:
            raise ValueError('String not in tree.')
