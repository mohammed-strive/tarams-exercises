class Node:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def getData(self):
        return self.__data

    def setData(self, newData):
        self.__data = newData

    def getLeftNode(self):
        return self.__left

    def setLeftNode(self, node):
        assert isinstance(node, Node) or node == None
        self.__left = node

    def getRightNode(self):
        return self.__right

    def setRightNode(self, node):
        assert isinstance(node, Node) or node == None
        self.__right = node

class BinaryTree:
    def __init__(self, node=None):
        if node:
            self.__root = Node(node)
        else:
            self.__root = None

def inorder(root):
    assert isinstance(root, Node) or root == None

    if root:
        inorder(root.getLeftNode())
        print(root.getData())
        inorder(root.getRightNode())

def preorder(root):
    assert isinstance(root, Node) or root == None

    if root:
        print(root.getData())
        preorder(root.getLeftNode())
        preorder(root.getRightNode())

def postorder(root):
    assert isinstance(root, Node) or root == None

    if root:
        postorder(root.getLeftNode())
        postorder(root.getRightNode())
        print(root.getData())


def height(root):
    if root is None:
        return 0

    left = height(root.getLeftNode())
    right = height(root.getRightNode())

    if left >= right:
        return left + 1
    else:
        return right + 1 

def levelorder(root):
    h = height(root)
    for i in range(1, h+1):
        printlevel(root, i)

def printlevel(node, h):
    if not node:
        return
    if h == 1:
        print(node.getData())
    else:
        printlevel(node.getLeftNode(), h-1)
        printlevel(node.getRightNode(), h-1)

if __name__ == '__main__':
    root = Node(1)
    root.setLeftNode(Node(2))
    root.setRightNode(Node(3))
    root.getLeftNode().setLeftNode(Node(4))
    root.getLeftNode().setRightNode(Node(5))

    inorder(root)
    preorder(root)
    postorder(root)
    levelorder(root)
