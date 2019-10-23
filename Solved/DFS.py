class Node:
    def __init__(self,name):
        self.children=[]
        self.name=name
    def addChildren(self,name):
        self.children.append(Node(name))
        return self
    def depthFirstSearch(self,array):
        array.append(self.name)
        for node in self.children:
            node.depthFirstSearch(array)
        return array
