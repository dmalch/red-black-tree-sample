from com.github.dmalch.abstractTreeTest import AbstractTreeTest
from com.github.dmalch.redBlackNode import Node
from com.github.dmalch.redBlackTree import RedBlackTree

__author__ = 'Dmitry'

import unittest


class TreeTest(unittest.TestCase, AbstractTreeTest):
    def getTree(self):
        tree = RedBlackTree()
        return tree

    def testInsertIntoASingleTwoNodeLeft(self):
        tree = self.getTree()
        tree.put(2, "2")
        tree.put(1, "1")

        root = tree._root

        self.assertEquals(root._value, "2")
        self.assertEquals(root._color, False)
        self.assertEquals(root._left._value, "1")
        self.assertEquals(root._left._color, True)

    def testInsertIntoASingleTwoNodeRight(self):
        tree = self.getTree()
        tree.put(1, "1")
        tree.put(2, "2")

        root = tree._root

        self.assertEquals(root._value, "2")
        self.assertEquals(root._color, False)
        self.assertEquals(root._left._value, "1")
        self.assertEquals(root._left._color, True)

    def testRotateLeft(self):
        node = Node(1, "1", False)
        node._left = Node(2, "2", False)
        red = Node(3, "3", True)
        node._right = red

        red._left = Node(4, "4", False)
        red._right = Node(5, "5", False)

        rotated = node.rotateLeft()

        self.assertEquals(rotated._value, "3")
        self.assertEquals(rotated._color, False)
        self.assertEquals(node._value, "1")
        self.assertEquals(node._color, True)

    def testRotateRight(self):
        node = Node(1, "1", False)
        red = Node(2, "2", True)
        node._left = red
        red._left = Node(3, "3", False)
        red._right = Node(4, "4", False)
        node._right = Node(5, "5", False)

        rotated = node.rotateRight()

        self.assertEquals(rotated._value, "2")
        self.assertEquals(rotated._color, False)
        self.assertEquals(node._value, "1")
        self.assertEquals(node._color, True)


if __name__ == '__main__':
    unittest.main()
