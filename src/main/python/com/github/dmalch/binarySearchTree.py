from com.github.dmalch.abstractTree import AbstractTree, Node


class BinarySearchTree(AbstractTree):
    _root = None

    def put(self, key:int, value:str):
        self._root = self._put(self._root, key, value)

    def _put(self, node:Node, key:int, value:str):
        if node is None:
            return Node(key, value)

        if key < node._key:
            node._left = Node(key, value)

        elif key > node._key:
            node._right = Node(key, value)

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
