"""Trie module for trie tree."""


class Node(object):
    """Node for trie tree."""

    def __init__(self, end_node=False):
        """Create instance of the node."""
        self.end = end_node
        self.prefix = 0
        self.children = {}


class Trie(object):
    """Trie (prefix tree) in python."""

    def __init__(self, iterable=()):
        """Create a trie instance."""
        self.root = Node()
        self.size = 0
        if isinstance(iterable, (list, tuple)):
            for word in iterable:
                self.insert(word)
        else:
            raise ValueError('Must be a list or tuple.')

    def insert(self, string):
        """Insert a word into the tree."""
        if not isinstance(string, str):
            raise ValueError('Must be a string.')
        curr = self.root
        for l in string:
            if l not in curr.children:
                curr.children[l] = Node()
            curr = curr.children[l]
            curr.prefix += 1
        curr.end = True
        self.size += 1

    def contains(self, string):
        """Check for word in the trie."""
        if not isinstance(string, str):
            raise ValueError('Can only search for a string.')
        curr = self.root
        for l in string:
            if l not in curr.children:
                return False
            curr = curr.children[l]
        return curr.end

    def remove(self, string):
        """Remove a word from the trie."""
        if not isinstance(string, str):
            raise ValueError('Can only search string.')
        curr = self.root
        stack = []
        for l in string:
            if l not in curr.children:
                raise ValueError('The word you entered is not in the trie.')
            stack.append(curr)
            curr = curr.children[l]
        if curr.end:
            self._erase_children(stack, string)
        else:
            raise ValueError('no such word exist in trie')

    def _erase_children(self, stack, string):
        """Helper function for removing the word."""
        reverse_word = string[::-1]
        i = -1
        for l in reverse_word:
            if len(stack[i].children[l].children) == 0:
                del stack[i].children[l]
            else:
                stack[i].children[l].end = False
                break
            i -= 1
        self.size -= 1

    def traversal_letter(self, start, curr=None):
        """."""
        if not isinstance(start, str):
            raise ValueError('Must be a string')
        curr = self.root
        for l in start:
            if l not in curr.children:
                return []
            curr = curr.children[l]
        return self._dfs_letter(curr, start)

    def _dfs_letter(self, node, start):
        """Search the tree with dfs to get letters."""
        if node.end:
            yield start
        for l in node.children:
            for word in self._dfs(node.children[l], l):
                for l in word:
                    yield l

    def traversal_word(self, start):
        """Generator for words with prefix of start or part of start."""
        if not isinstance(start, str):
            raise ValueError('can only traverse form a string')
        curr = self.root
        for l in start:
            if l not in curr.children:
                return []
            curr = curr.children[l]
        return self._dfs(curr, start)

    def _dfs(self, node, start):
        """Extra Credit: Search the tree with dfs to form words."""
        if node.end:
            yield start
        for letter in node.children:
            for word in self._dfs(node.children[letter], start + letter):
                yield word

    def size(self):
        """Return the size of current prefix tree."""
        return self.size
