class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(self,data):
    if self.data:
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
    else:
        self.data = data