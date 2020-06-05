import collections

class Queue:
    def __init__(self, *items):
        if items:
            self.__queue = collections.deque(items)
        else:
            self.__queue = collections.deque()

    def enqueue(self, item):
        return self.__queue.append(item)

    def dequeue(self):
        return self.__queue.popleft()

    def __repr__(self):
        return "Queue({!r})".format(self.__queue)

    def __str__(self):
        string = ", ".join(map(str, self.__queue))
        return "[{}]".format(string)

if __name__ == '__main__':
    queue = Queue(1, 2, 3, 4, 5)
    queue.enqueue(10)
    print(queue.dequeue())
    print(queue)
