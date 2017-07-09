from node import Node
class LinkedList(object):
    def __init__(self):
        self.__first = None

    def __node_at(self, position):
        i = 0
        pointer = self.__first
        while(i < position):
            pointer = pointer.next_node
            i = i + 1
        return pointer

    def __contains__(self, element):
        for e in self:
            if(e == element):
                return True
        return False

    def element_at(self, index):
        if (index >= len(self)):
            return False
        pointer = self.__node_at(index)
        return pointer.data

    def __iter__(self):
        pointer = self.__first
        while(pointer != None):
            yield pointer.data
            pointer = pointer.next_node

    def __len__(self):
        count = 0
        for e in self:
            count += 1
        return count
    
    def insert(self, position, element):
        if (len(self) == 0):
            n = Node(element, None)
            self.__first = n
            return
    
        pointer = self.__node_at(position - 1)
        n = Node(element, None)
        n.next_node = pointer.next_node
        pointer.next_node = n
