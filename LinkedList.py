class Node(object):
    def __init__(self, data, node=None):
        self.__data = data
        self.__next = node

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getNextNode(self):
        return self.__next

    def setNextNode(self, node):
        assert isinstance(node, Node)
        self.__next = node

    def __repr__(self):
        return "Node({})".format(self.__data,)

    def __str__(self):
        return "Node({})".format(self.__data,)

class LinkedList:
    def __init__(self, seed):
        assert isinstance(seed, Node)
        self.__head = seed

    def insert(self, data):
        newNode = Node(data)
        newNode.setNextNode(self.__head)
        self.__head = newNode

    def size(self):
        count = 0
        current = self.__head
        while current:
            count += 1
            current = current.getNextNode()
        return count

    def search(self, data):
        current = self.__head
        while current:
            if current.getData() == data:
                return current
            current = current.getNextNode()
        return False

    def remove(self, data):
        current = self.__head
        found = False
        prev = None

        while not found and current:
            if current.getData() == data:
                found = True
            else:
                prev = current
                current = current.getNextNode()

        if current is None:
            return None
        if prev is None:
            self.__head = current.getNextNode()
        else:
            prev.setNextNode(current.getNextNode())

    def __str__(self):
        current = self.__head

        while current is not None:
            print(current.getData())
            current = current.getNextNode()

if __name__ == '__main__':
    linklist = LinkedList(Node(9))
    linklist.insert(Node(100))
    print(linklist.size())
