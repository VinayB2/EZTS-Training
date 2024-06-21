class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
root = Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6), right=Node(7)))
def zigZag(node):
    rev = False
    queue = [node]
    lst = []
    while len(queue) != 0:
        h = len(queue)
        l = []
        for i in range(h):
            if not rev:
                e = queue.pop(0)
            else:
                e = queue.pop()
            l.append(e.data)
            if not rev:
                if e.left != None:
                    queue.append(e.left)
                if e.right != None:
                    queue.append(e.right)
            else:
                if e.right != None:
                    queue.insert(0, e.right)
                if e.left != None:
                    queue.insert(0, e.left)
        rev = not rev
        lst.append(l)
    return lst
print(zigZag(root))