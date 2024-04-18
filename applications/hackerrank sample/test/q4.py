class node():
    def __init__(self,num, parent):
        self.num = num
        self.parent = parent #None if root, node
        self.children = []
        
    def add_child(self, childNum, weight):
        child = node(childNum, self)
        self.children.append(child)