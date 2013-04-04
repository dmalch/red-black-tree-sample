from com.github.dmalch.abstractTreeTest import AbstractTreeTest
from com.github.dmalch.binarySearchTree import BinarySearchTree

__author__ = 'Dmitry'

import unittest


class TreeTest(unittest.TestCase, AbstractTreeTest):
    def getTree(self):
        tree = BinarySearchTree()
        return tree


if __name__ == '__main__':
    unittest.main()
