from com.github.dmalch.binarySearchTree import BinarySearchTree

__author__ = 'Dmitry'

import unittest


class TreeTest(unittest.TestCase):
    def testTree(self):
        tree = BinarySearchTree()
        expectedValue = "1"

        tree.put(1, expectedValue)

        self.assertEqual(tree.get(1), expectedValue)

    def testTree2(self):
        tree = BinarySearchTree()
        tree.put(1, "1")
        tree.put(2, "2")

        self.assertEqual(tree.get(1), "1")
        self.assertEqual(tree.get(2), "2")

    def testTree3(self):
        tree = BinarySearchTree()
        tree.put(2, "2")
        tree.put(1, "1")
        tree.put(3, "3")

        self.assertEqual(tree.get(1), "1")
        self.assertEqual(tree.get(2), "2")
        self.assertEqual(tree.get(3), "3")

    def testTree3(self):
        tree = BinarySearchTree()
        tree.put(1, "1")
        tree.put(2, "2")
        tree.put(2, "3")

        self.assertEqual(tree.get(2), "3")


if __name__ == '__main__':
    unittest.main()
