class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.height = 1
def inOrder(node):
    if not node:
        return
    inOrder(node.left)
    print(node.value, end = " ")
    inOrder(node.right)

def height(node):
    if node == None:
        return 0
    return node.height

def getBF(node):
    if node == None:
        return 0
    return height(root.left) - height(root.right)

def leftRotate(A):
    B = A.right
    temp = B.left
    B.left = A
    A.right = temp
    A.height = 1 + max(height(A.left), height(A.right))
    B.height = 1 + max(height(B.left), height(B.right))
    return B

def rightRotate(A):
    B = A.left
    temp = B.right
    B.right = A
    A.left = temp
    A.height = 1 + max(height(A.left), height(A.right))
    B.height = 1 + max(height(B.left), height(B.right))
    return B

def insert(root, i):
    if not root:
        return Node(i)
    
    if i < root.value:
        root.left = insert(root.left, i)

    if i > root.value:
        root.right = insert(root.right, i)

    root.height = 1 + max(height(root.left), height(root.right))
    BF = getBF(root)
    
    if BF > 1 and i < root.left.value: 
        return rightRotate(root)
    
    if BF > 1 and i > root.left.value:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    
    if BF < -1 and i > root.right.value:
        return leftRotate(root)
    
    if BF < -1 and i < root.right.value:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    
    return root

if __name__ == "__main__":
    VL = [19, 99, 75, 7, 21, 34, 38, 47, 134, 100, 29, 0, 12, 17, 143]
    root = None
    for i in VL:
        root = insert(root, i)
    inOrder(root)