import collections

class Stack(object):
    def __init__(self, *items):
        if items:
            self.__stack = collections.deque(items)
        else:
            self.__stack = collections.deque()

    def pop(self):
        try:
            return self.__stack.pop()
        except IndexError:
            return None

    def push(self, item):
        self.__stack.append(item)

    def __repr__(self):
        return "Stack({!r})".format(self.__stack)

    def __str__(self):
        string = ", ".join(map(str, self.__stack))
        return "[{}]".format(string)

if __name__ == '__main__':
    stack = Stack(1, 2, 3, 4, 5)
    stack.push(100)
    print(stack)
    stack.pop()
    print(stack)
