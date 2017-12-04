"""Module for a Hash table."""


class HT(object):
    """Class for hash table."""

    def __init__(self, size=1024, hash_func='additive'):
        """Hash table constructor."""
        self.size = size
        self.hash_func = hash_func
        self.h_table = [[] for i in range(size)]

    def get(self, key):
        """Use key to get value from table."""
        hash_key = self._hash(key)
        for i in self.h_table[hash_key]:
            if i[0] == key:
                return i[1]

    def set(self, key, value):
        """Put the hash in a bucket."""
        if isinstance(key, str):
            hash_key = self._hash(key)
            self.h_table[hash_key].append([key, value])
        else:
            raise TypeError('The key must be a string')

    def _hash_additive(self, key):
        """Additive method."""
        val = 0
        for i in key:
            val += ord(i)
        return val % self.size

    def _hash_bernstein(self, key):
        """Simple Bernstein method."""
        val = 200
        for i in key:
            val = ((val << 5) + val) + ord(i)
        return val % self.size

    def _hash_fnv(self, key):
        """Simple FNV hash."""
        val = 2166
        for i in key:
            val = (val * 167) ^ ord(i)
        return val

    def _hash_sax(self, key):
        """Shift-add-XOR hash."""
        val = 0
        for i in key:
            val ^= (val << 5) + (val >> 2) + ord(i)
        return val

    def _hash(self, key):
        """Holiday hash maker."""
        if self.hash_func == 'additive':
            return self._hash_additive(key)
        elif self.hash_func == 'bernstein':
            return self._hash_bernstein(key)
        elif self.hash_func == 'fnv':
            return self._hash_fnv(key)
        elif self.hash_func == 'sax':
            return self._hash_sax(key)
