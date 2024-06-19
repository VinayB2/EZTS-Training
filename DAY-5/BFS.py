from queue import Queue
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
        self._size -= 1
        return self._items.pop(0)
        # return data
    def isEmpty(self):
        return self._size == 0
    def size(self):
        return self._size
    def get_data(self):
        return self._items

class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

def BFS(node):
    queue = Queue()
    queue.push(node)
    while not queue.isEmpty():
        if queue.size == 1 and queue.peek == None:
            return
        e = queue.pop()
        print(e.data, end = " ")
        if not e.left == None :
            queue.push(e.left)
        if not e.right == None:
            queue.push(e.right)
def BFS2(node):
    Q = [node]
    Q.append(None)
    while len(Q) > 0:
        curr = Q.pop(0)
        if curr == None:
            if len(Q) == 0:
                break
            else:
                print()
                Q.append(None)
        else:
            print(curr.data, end = " ")
            if curr.left != None:
                Q.append(curr.left)
            if curr.right != None:
                Q.append(curr.right) 
BFS2(root)