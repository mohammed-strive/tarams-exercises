class Array(object):
    def __init__(self, *items):
        if items:
            self.__array = [item for item in items]
        else:
            self.__array = []

    def __len__(self):
        return len(self.__array)

    def append(self, item):
        self.__array.append(item)

    def __getitem__(self, index):
        return self._array[index]

    def extend(self, items):
        self.__array.extend(items)

    def contains(self, item):
        return self.__array.index(item)

    def remove(self, index):
        if index < 0 or index > len(self.__array):
            return -1
        newArray = []
        for i in range(len(self.__array)):
            if i == index:
                item = self.__array[index]
            newArray.append(self.__array[i])

        self.__array = newArray
        return item

    def __repr__(self):
        return "Array({!r})".format(*self.__array)

    def __str__(self):
        string = ",".join(map(str, self.__array))
        return "[{}]".format(string,)

if __name__ == '__main__':
    arr = Array(1, 2, 3, 4, 5)
    arr.append(6)
    arr.extend((90, 34))
    print(arr)
