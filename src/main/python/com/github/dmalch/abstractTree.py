class AbstractTree:
    def put(self, key:int, value:str):
        pass

    def get(self, key:int):
        pass


class Node:
    _key = None
    _value = None
    _left = None
    _right = None

    def __init__(self, key:int, value:str):
        self._key = key
        self._value = value