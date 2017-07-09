class Queue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self, element):
        self.__list.append(element)

    def dequeue(self):
        tmp = self.__list[0]
        self.__list = self.__list[1: len(self.__list)]
        return tmp

    def peek(self):
        return self.__list[0]