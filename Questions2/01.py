class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
root = Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6), right=Node(7)))
def printTree(node):
    if node == None:
        return
    print(node.data)
    printTree(node.left)
    printTree(node.right)
def height(node):
    if node == None:
        return 0
    return max(height(node.left), height(node.right)) + 1
def BFS(node):
    queue = [node]
    lst = []
    while len(queue) != 0:
        h = len(queue)
        l = []
        for i in range(h):
            curr = queue.pop(0)
            l.append(curr.data)
            if curr.left != None:
                queue.append(curr.left)
            if curr.right != None:
                queue.append(curr.right)
        lst.append(l)
    return lst
def rightView(node):
    queue = [node]
    lst = []
    while len(queue) != 0:
        h = len(queue)
        l = []
        for i in range(h):
            curr = queue.pop(0)
            if i == h - 1:
                print(curr.data)
            if curr.left != None:
                queue.append(curr.left)
            if curr.right != None:
                queue.append(curr.right)

def average_levels(node):
    lst = []
    queue = [node]
    while len(queue) != 0:
        sum = 0.0
        h = len(queue)
        for i in range(h):
            e = queue.pop(0)
            sum += e.data
            if e.left != None:
                queue.append(e.left)
            if e.right != None:
                queue.append(e.right)
        lst.append(sum / h)
    return lst
global dia
dia = 0
def diameterOfBinaryTree(root):
    diaHelper(root)
    return dia
def diaHelper(node):
    if node == None:
        return 0
    left = diaHelper(node.left)
    right = diaHelper(node.right)
    global dia
    dia = max(dia, left + right)
    return max(left, right) + 1

def zig_zag(root):
    rev = False
    queue = [root]
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
                if e.right != None:
                    queue.append(e.right)
                if e.left != None:
                    queue.append(e.left)
            else:
                if e.left != None:
                    queue.insert(0,e.left)
                if e.right != None:
                    queue.insert(0,e.right)
        rev = not rev
        lst.append(l)
    return lst
print(rightView(root))