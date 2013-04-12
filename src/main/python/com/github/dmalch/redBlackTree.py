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
            if node._left._color and node._left._left and node._left._left._color:
                rotated = node.rotateRight()
                rotated._left._color = False
                rotated._right._color = False
                rotated._color = True
                return rotated

        elif key > node._key:
            node._right = self._put(node._right, key, value)
            if node._right._color and node._left and node._left._color:
                node._left._color = False
                node._right._color = False
            elif node._right._color:
                return node.rotateLeft()
        else:
            node._value = value

        return node

    def get(self, key:int):
        return self._get(self._root, key)

    def _get(self, node:Node, key:int):
        if node is None:
            return None

        if key < node._key:
            return self._get(node._left, key)

        elif key > node._key:
            return self._get(node._right, key)

        else:
            return node._value
