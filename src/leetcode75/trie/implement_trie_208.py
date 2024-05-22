class TrieNode:

    def __init__(self):
        self.is_leaf = False
        self.children = dict()


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        node = self.root

        for c in word:

            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.is_leaf = True

    def search(self, word: str) -> bool:

        node = self.root

        for c in word:
            node = node.children.get(c)
            if not node:
                return False

        return node.is_leaf

    def startsWith(self, prefix: str) -> bool:

        node = self.root

        for c in prefix:
            node = node.children.get(c)
            if not node:
                return False

        return True
