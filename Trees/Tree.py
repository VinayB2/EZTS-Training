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

def preOrder(node):
    if node == None:
        return
    print(node.data, end = " ")
    preOrder(node.left)
    preOrder(node.right)

def postOrder(node):
    if node == None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.data, end = " ")

def inOrder(node):
    if node == None:
        return
    inOrder(node.left)
    print(node.data, end = " ")
    inOrder(node.right)
    
preOrder(root)
print()
postOrder(root)
print()
inOrder(root)