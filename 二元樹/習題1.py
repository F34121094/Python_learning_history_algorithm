class Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None


    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left :
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

    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def count(self,time):
        a = time
        l,r = 0,0
        if not self.left:
            l += 1
        if not self.right:
            r += 1
        if l == 1 and r == 1: a += 1
        if l == 0: self.left.count(a)
        if r == 0: self.right.count(a)
        return a

tree = Node()
datas = [10,5,21,9,13,28,3,4,1,17,32]
for i in datas:
    tree.insert(i)
time = 0
tree.preorder()
print(f"葉節點數量 = {tree.count(time)}")
