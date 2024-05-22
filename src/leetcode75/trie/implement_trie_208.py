from typing import Self, Optional


class TrieNode:

    def __init__(self, is_leaf=False, value=None):
        self.is_leaf = is_leaf
        self.value = value
        self.children = dict()

    def add_child(self, key: str, node: Self) -> None:

        if not key:
            raise ValueError('Cannot insert empty key')

        self.children[key] = node

    def get_child(self, key: str) -> Optional[Self]:

        if not key:
            raise ValueError('Cannot retrieve empty key')

        return self.children.get(key, None)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        if not self.value:
            return "root"

        return self.value

    def has_child(self, key):
        return key in self.children


class Trie:

    def __init__(self):
        self.root = TrieNode(value="")

    def insert(self, word: str) -> None:

        if not str:
            raise ValueError('Cannot insert empty value')

        node = self.root

        for c in word:
            if node.has_child(c):
                node = node.get_child(c)
            else:
                child = TrieNode(value=c)
                node.add_child(c, child)
                node = child

        node.is_leaf = True

    def search(self, word: str) -> bool:

        node = self.root

        for c in word:
            node = node.get_child(c)
            if not node:
                return False

        return node.is_leaf

    def startsWith(self, prefix: str) -> bool:

        node = self.root

        for c in prefix:
            node = node.get_child(c)
            if not node:
                return False

        return True
