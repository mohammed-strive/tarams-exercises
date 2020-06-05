class Node:
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
        assert isinstance(node, Node) or node == None
        self.__next = node

    def __repr__(self):
        return "Node({})".format(self.__data,)

    def __str__(self):
        return "Node({})".format(self.__data,)

class LinkedList:
    def __init__(self, head):
        if head:
            assert isinstance(head, Node)
            self.__head = head
        else:
            self.__head = None

    def __iter__(self):
        return self

    def __next__(self):
        current = self.__head
        while current:
            return current.getData()
            current = current.getNextNode()
        else:
            raise StopIteration

    def insert_at_start(self, data):
        newNode = Node(data)
        newNode.setNextNode(self.__head)
        self.__head = newNode

    def insert_at_end(self, data):
        newNode = Node(data)

        if self.__head is None:
            self.__head = newNode
            return

        current = self.__head

        while current.getNextNode() is not None:
            current = current.getNextNode()
        current.setNextNode(newNode)

    def insert_after_item(self, nodeData, newData):
        current = self.__head

        while current:
            if current.getData() == nodeData:
                break
            current = current.getNextNode()
        if current is None:
            raise ValueError

        newNode = Node(newData)
        newNode.setNextNode(current.getNextNode())
        current.setNextNode(newNode)

    def insert_before_item(self, nodeData, newData):
        current = self.__head

        if current is None:
            raise ValueError

        prev = None
        while current:
            if current.getData() == nodeData:
                break
            prev = current
            current = current.getNextNode()

        if current is None:
            raise ValueError

        newNode = Node(newData)
        if not prev:
            newNode.setNextNode(current)
            self.__head = newNode
            return
        prev.setNextNode(newNode)
        newNode.setNextNode(current)

    def insert_at_index(self, index, newData):
        if index == 0:
            return self.insert_at_start(newData)

        current = self.__head

        curIndex = 0
        while (index - 1 != curIndex) and current:
            current = current.getNextNode()
            curIndex += 1

        if not current and index != 0:
            raise IndexError

        newNode = Node(newData)
        newNode.setNextNode(current.getNextNode())
        current.setNextNode(newNode)


    def traverse(self):
        if not self.__head:
            print("No element")
            return
        else:
            current = self.__head
            while current:
                print(current.getData(), " ")
                current = current.getNextNode()

    def search_item(self, data):
        current = self.__head

        while current:
            if current.getData() == data:
                return True
            current = current.getNextNode()

        return False

    def delete_item_by_value(self, value):
        current = self.__head

        prev = None
        while current:
            if current.getData() == value:
                break
            prev = current
            current = curren.getNextNode()

        if current and not prev:
            self.__head = current.getNextNode()
            return

        prev.setNextNode(current.getNextNode())
        return

    def delete_item_by_index(self, index):
        current = self.__head

        if not current:
            raise IndexError

        curIndex = 0
        prev = None
        while current and curIndex != index:
            if curIndex == index:
                break
            prev = current
            current = current.getNextNode()
            curIndex += 1

        if index == 0 and not prev and current:
            self.__head = current.getNextNode()
            return

        prev.setNextNode(current.getNextNode())
        return

    def delete_item_at_start(self):
        return self.delete_item_by_index(0)

    def delete_item_at_end(self):
        pass

    def reverse(self):
        current = self.__head
        prev = None
        nxt = None

        while current:
            nxt = current.getNextNode()
            current.setNextNode(prev)
            prev = current
            current = nxt

        self.__head = prev

if __name__ == '__main__':
    linkedList = LinkedList(Node(10))
    linkedList.insert_at_start(20)
    linkedList.insert_at_start(30)
    linkedList.insert_at_end(50)
    linkedList.insert_before_item(20, 25)
    linkedList.insert_after_item(20, 35)
    linkedList.insert_after_item(50, 55)
    linkedList.insert_after_item(30, 45)
    linkedList.insert_before_item(30, 22)
    linkedList.insert_at_index(3, 100)
    linkedList.insert_at_index(1, 400)
    linkedList.delete_item_by_index(5)
    linkedList.reverse()
    linkedList.traverse()
