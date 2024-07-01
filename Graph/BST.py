class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertBST(lst):
    root = None
    for i in  lst:
        root = insert(root, i)
    printTree(root)

def printTree(node):
    if node == None:
        return
    printTree(node.left)
    print(node.val)
    printTree(node.right)

def insert(root, val):
    if root == None:
        return Node(val)
    if val > root.val:
        root.right = insert(root.right, val)
    if val < root.val:
        root.left = insert(root.left, val)
    if val == root.val:
        return
    return root

lst = [4, 6, 7, 3, 8, 2, 5, 9, 1]
insertBST(lst)