from com.github.dmalch.abstractTree import AbstractTree


class RedBlackTree(AbstractTree):
    def put(self, key:int, value:str):
        super().put(key, value)

    def get(self, key:int):
        super().get(key)

