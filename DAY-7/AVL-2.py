class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    if node == None:
        return -1
    return node.height


def rightRotate(p):
    c = p.left
    tmp = c.right
    c.right = p
    p.left = tmp
    p.height = max(height(p.left), height(p.right) + 1)
    c.height = max(height(c.left), height(c.right) + 1)
    return c

def leftRotate(p):
    c = p.right
    tmp = c.left
    c.left = p
    p.right = tmp
    p.height = max(height(p.left), height(p.right) + 1)
    c.height = max(height(c.left), height(c.right) + 1)
    return c

def rotate(node):
    if height(node.left) - height(node.right) > 1:
        # Right heavy
        if height(node.left.left) - height(node.left.right) > 0:
            # Left Left case
            return rightRotate(node)
        if height(node.left.left) - height(node.left.right) < 0:
            # Left Right case
            node.left = leftRotate(node.left)
            return rightRotate(node)
    if height(node.left) - height(node.right) < -1:
        # Right heavy
        if height(node.right.left) - height(node.right.right) < 0:
            # Right Right case
            return leftRotate(node)
        if height(node.right.left) - height(node.right.right) > 0:
            # Right Left case
            node.right = rightRotate(node.right)
            return leftRotate(node)
    return node

def insert(node, val):
    if node == None:
        return Node(val)
    if val < node.value:
        node.left = insert(node.left, val)
    if val > node.value:
        node.right = insert(node.right, val)
    
    node.height = max(height(node.left), height(node.right)) + 1
    return rotate(node)

def inOrder(node):
    if node == None:
        return
    inOrder(node.left)
    print(node.value)
    inOrder(node.right)

def levelOrder(root):
    ans = []
    queue = [root]
    while len(queue) != 0:
        lev = []
        h = len(queue)
        for i in range(h):
            e = queue.pop(0)
            lev.append(e)
            if e.left != None:
                queue.append(e.left)
            if e.right != None:
                queue.append(e.right)
        ans.append(lev)
    return ans


if __name__ == "__main__":
    lst = [1,5,2,3,7,8,9]
    root = None
    for i in lst:
        root = insert(root, i)
    print(levelOrder(root))