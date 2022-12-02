class Stack:

    def __init__(self):
        self.__list = []
        self.__length = -1

    def getStack(self):
        return self.__list

    def getLength(self):
        return self.__length

    def push(self, value):
        self.__list.append(value)
        self.__length += 1

    def pop(self):
        if self.__length == -1:
            return 0
        else:
            self.__length -= 1
            return self.__list.pop()

    def seek(self):
        return False if self.__length == -1 else self.__list[self.__length]
