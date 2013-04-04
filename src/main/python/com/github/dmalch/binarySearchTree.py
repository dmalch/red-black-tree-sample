__author__ = 'Dmitry'


class BinarySearchTree:
    class TreeNode:
        _key = None
        _value = None
        _left = None
        _right = None

        def __init__(self, key:int, value:str):
            self._key = key
            self._value = value

    _root = None

    def put(self, key:int, value:str):
        self._root = self._put(self._root, key, value)

    def _put(self, node, key:int, value:str):
        if node is None:
            return self.TreeNode(key, value)

        if key < node._key:
            node._left = self.TreeNode(key, value)

        elif key > node._key:
            node._right = self.TreeNode(key, value)

        else:
            node._value = value

        return node

    def get(self, key:int):
        return self._get(self._root, key)

    def _get(self, node, key:int):
        if node is None:
            return None

        if key < node._key:
            return self._get(node._left, key)

        elif key > node._key:
            return self._get(node._right, key)

        else:
            return node._value
