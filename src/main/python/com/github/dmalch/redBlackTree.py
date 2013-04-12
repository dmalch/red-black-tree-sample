from com.github.dmalch.abstractTree import AbstractTree
from com.github.dmalch.redBlackNode import Node


class RedBlackTree(AbstractTree):
    _root = None

    def put(self, key:int, value:str):
        self._root = self._put(self._root, key, value)
        self._root._color = False

    def _put(self, node:Node, key:int, value:str):
        if node is None:
            return Node(key, value, True)

        if key < node._key:
            node._left = self._put(node._left, key, value)

        elif key > node._key:
            node._right = self._put(node._right, key, value)

        else:
            node._value = value

        return node


    def get(self, key:int):
        super().get(key)
