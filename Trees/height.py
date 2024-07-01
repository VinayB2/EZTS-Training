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

root.right.right.right = TreeNode(10)


def height(node):
    if node == None:
        return 0
    return max(height(node.left), height(node.right) + 1)

def printLeaves(node):
    if node == None:
        return
    if node.left == None and node.right == None:
        print(node.data, end = " ")
        return
    printLeaves(node.left)
    printLeaves(node.right)

def leftView(node):
    print(node.data)
    Q = [node]
    Q.append(None)
    l = []
    while len(Q) > 0:
        curr = Q.pop(0)
        if curr == None:
            if len(Q) == 0:
                break
            else:
                Q.append(None)
                print(Q[0].data)

        else:
            l.append(curr.data)
            if curr.left != None:
                Q.append(curr.left)
            if curr.right != None:
                Q.append(curr.right)
class Node_Data:
    def __init__(self, Node, Hkey):
        self.node = Node
        self.Hkey = Hkey

def topView(node):
    temp = Node_Data(node, 0)
    Q = [temp]
    Q.append(None)
    key_dict = {}
    while len(Q) != 0:
        curr = Q.pop(0)
        if curr == None:
            if len(Q) == 0:
                break
            else:
                Q.append(None)
        else:
            if curr.Hkey not in key_dict.keys():
                key_dict[curr.Hkey] = curr.node.data
            if curr.node.left != None:
                tmp = Node_Data(curr.node.left, curr.Hkey - 1)
                Q.append(tmp)
            if curr.node.right != None:
                tmp = Node_Data(curr.node.right, curr.Hkey + 1)
                Q.append(tmp)
    for i in sorted(key_dict.keys):
        print(key_dict[i])
def bottomView(node):
    temp = Node_Data(node, 0)
    Q = [temp]
    Q.append(None)
    key_dict = {}
    while len(Q) != 0:
        curr = Q.pop(0)
        if curr == None:
            if len(Q) == 0:
                break
            else:
                Q.append(None)
        else:
            key_dict[curr.Hkey] = curr.node.data
            if curr.node.left != None:
                tmp = Node_Data(curr.node.left, curr.Hkey - 1)
                Q.append(tmp)
            if curr.node.right != None:
                tmp = Node_Data(curr.node.right, curr.Hkey + 1)
                Q.append(tmp)
    for i in sorted(key_dict.keys()):
        print(key_dict[i])


leftView(root)