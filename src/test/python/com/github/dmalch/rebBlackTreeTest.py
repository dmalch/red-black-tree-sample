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

    def testInsertIntoATwoNodeAtTheBottom(self):
        tree = self.getTree()
        tree.put(3, "3")
        root = tree._root
        root._left = Node(1, "1", False)

        tree.put(2, "2")
        root = tree._root

        self.assertEquals(root._value, "3")
        self.assertEquals(root._color, False)
        self.assertEquals(root._left._value, "2")
        self.assertEquals(root._left._color, False)
        self.assertEquals(root._left._left._value, "1")
        self.assertEquals(root._left._left._color, True)

    def testInsertIntoAThreeNodeWhenKeyIsLarger(self):
        tree = self.getTree()
        tree.put(2, "2")
        tree.put(1, "1")
        tree.put(3, "3")
        root = tree._root

        self.assertEquals(root._value, "2")
        self.assertEquals(root._color, False)
        self.assertEquals(root._right._value, "3")
        self.assertEquals(root._right._color, False)
        self.assertEquals(root._left._value, "1")
        self.assertEquals(root._left._color, False)

    def testInsertIntoAThreeNodeWhenKeyIsSmaller(self):
        tree = self.getTree()
        tree.put(3, "3")
        tree.put(2, "2")
        tree.put(1, "1")
        root = tree._root

        self.assertEquals(root._value, "2")
        self.assertEquals(root._color, False)
        self.assertEquals(root._right._value, "3")
        self.assertEquals(root._right._color, False)
        self.assertEquals(root._left._value, "1")
        self.assertEquals(root._left._color, False)

    def testInsertIntoAThreeNodeWhenKeyIsBetween(self):
        tree = self.getTree()
        tree.put(3, "3")
        tree.put(1, "1")
        tree.put(2, "2")
        root = tree._root

        self.assertEquals(root._value, "2")
        self.assertEquals(root._color, False)
        self.assertEquals(root._right._value, "3")
        self.assertEquals(root._right._color, False)
        self.assertEquals(root._left._value, "1")
        self.assertEquals(root._left._color, False)

    def testInsertIntoAThreeNodeAtTheBottom(self):
        tree = self.getTree()
        tree.put(3, "3")
        root = tree._root
        root._left = Node(2, "2", False)
        root._left._left = Node(1, "1", True)
        root._right = Node(6, "6", False)
        root._right._left = Node(5, "5", True)

        tree.put(4, "4")
        root = tree._root

        self.assertEquals(root._value, "5")
        self.assertEquals(root._color, False)
        self.assertEquals(root._right._value, "6")
        self.assertEquals(root._right._color, False)
        self.assertEquals(root._left._value, "3")
        self.assertEquals(root._left._color, True)
        self.assertEquals(root._left._left._value, "2")
        self.assertEquals(root._left._left._color, False)
        self.assertEquals(root._left._left._left._value, "1")
        self.assertEquals(root._left._left._left._color, True)
        self.assertEquals(root._left._right._value, "4")
        self.assertEquals(root._left._right._color, False)

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
