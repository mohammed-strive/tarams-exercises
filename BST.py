class Node:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def getData(self):
        return self.__data

    def set(self, newData):
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

    def __str__(self):
        return "Node({})".format(self.__data)

class BST:
    def __init__(self, root):
        assert isinstance(root, Node)
        self.__root = root

    @staticmethod
    def search(node, key):
        if not node: return node

        if node.getData() == key: return node

        if node.getData() < key:
            return BST.search(node.getRightNode(), key)
        return BST.search(node.getLeftNode(), key)

    @staticmethod
    def insert(node, data):
        newNode = Node(data)

        if not node:
            node = newNode
        else:
            if data > node.getData():
                if not node.getRightNode():
                    node.setRightNode(newNode)
                else:
                    BST.insert(node.getRightNode(), data)
            elif data < node.getData():
                if not node.getLeftNode():
                    node.setLeftNode(newNode)
                else:
                    BST.insert(node.getLeftNode(), data)

        return

    @staticmethod
    def inorder(root):
        if root:
            BST.inorder(root.getLeftNode())
            print(root.getData())
            BST.inorder(root.getRightNode())

if __name__ == '__main__':
    root = Node(8)

    tree = BST(root)
    tree.insert(root, 3)
    tree.insert(root, 10)
    tree.insert(root, 6)
    tree.insert(root, 1)
    tree.insert(root, 4)
    tree.insert(root, 7)
    print(tree.search(root, 10))
    tree.inorder(root)
