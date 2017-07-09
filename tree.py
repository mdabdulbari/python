class Node(object):
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

class Tree(object):
    
    def __init__(self, root = None):
        self.__root = root
