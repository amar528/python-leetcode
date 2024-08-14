from unittest import TestCase

from leetcode75.trie.implement_trie_208 import Trie


class TestTrie(TestCase):
    def test_trie_example1(self):
        under_test = Trie()

        under_test.insert("apple")
        self.assertTrue(under_test.search("apple"))
        self.assertFalse(under_test.search("app"))

        self.assertTrue(under_test.startsWith("app"))

        under_test.insert("app")
        self.assertTrue(under_test.search("app"))

    def test_trie_example2(self):
        under_test = Trie()

        under_test.insert("apple")
        under_test.insert("app")
        under_test.insert("beer")
        under_test.insert("add")
        under_test.insert("jam")
        under_test.insert("rental")

        self.assertFalse(under_test.search("apps"))
        self.assertTrue(under_test.search("app"))
        self.assertFalse(under_test.search("ad"))
        self.assertFalse(under_test.search("applepie"))
        self.assertFalse(under_test.search("rest"))
        self.assertFalse(under_test.search("jan"))
        self.assertFalse(under_test.search("rent"))
        self.assertTrue(under_test.search("beer"))
        self.assertTrue(under_test.search("jam"))
        self.assertFalse(under_test.startsWith("apps"))
        self.assertTrue(under_test.startsWith("app"))
        self.assertTrue(under_test.startsWith("ad"))
        self.assertFalse(under_test.startsWith("applepie"))
        self.assertFalse(under_test.startsWith("rest"))
        self.assertFalse(under_test.startsWith("jan"))
        self.assertTrue(under_test.startsWith("rent"))
        self.assertTrue(under_test.startsWith("beer"))
        self.assertTrue(under_test.startsWith("jam"))