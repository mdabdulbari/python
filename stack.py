class Stack(object):
    def __init__(self):
        self.__list = []

    def push(self, element):
        self.__list.append(element)

    def pop(self):
        tmp = self.__list[len(self.__list) - 1]
        self.__list = self.__list[0: len(self.__list)- 1]
        return tmp

    def peek(self):
        return self.__list[len(self.__list) - 1]