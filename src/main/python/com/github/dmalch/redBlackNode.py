class Node:
    _key = None
    _value = None
    _left = None
    _right = None
    _color = None

    def __init__(self, key:int, value:str, color:bool):
        self._key = key
        self._value = value
        self._color = color

    def rotateLeft(self):
        right = self._right
        self._right = right._left
        right._left = self
        right._color = self._color
        self._color = True

        return right

    def rotateRight(self):
        left = self._left
        self._left = left._right
        left._right = self
        left._color = self._color
        self._color = True

        return left
