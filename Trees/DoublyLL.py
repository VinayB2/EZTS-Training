class Node:
    def __init__(self, data = None, prev = None, next = None):
        self._data = data
        self._prev = prev
        self._next = next
class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0