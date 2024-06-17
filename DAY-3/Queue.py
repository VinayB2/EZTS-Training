class Queue(Exception):
    def __init__(self):
        self._items = []
        self._size = 0
    def push(self, data):
        self._items.append(data)
        self._size += 1
        return data
    def peek(self):
        return self._items[0]
    def pop(self):
        if(self._size == 0):
            raise Exception("Cant pop an empty stack")
        data = self._items[self._size - 1]
        self._items.pop(0)
        self._size -= 1
        return data
    def isEmpty(self):
        return self._size == 0
    def size(self):
        return self._size
    def get_data(self):
        return self._items