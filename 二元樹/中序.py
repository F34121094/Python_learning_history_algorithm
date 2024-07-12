class Node():
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data:
            if data < self.data:       #如果傳入的值比根節點值小，到左邊
                if self.left:
                    self.left.insert(data)      #如果現在左邊有東西，插入左邊
                else:
                    self.left = Node(data)      #左邊沒有東西，變成左1
            else:
                if self.right:          #如果傳入的值比根結點大，到右邊
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data
    def inorder(self):
        if self.left:
            self.left.inorder()     #如果左邊有東西，進行遞迴
        print(self.data)
        if self.right:
            self.right.inorder()

tree = Node()
datas = [10,21,5,9,13,28]
for d in datas:
    tree.insert(d)      #把二元樹的資料傳給Node()
tree.inorder()
#第一次進入時，因為self.data裡面沒有東西，所以會先else，然後傳第二個
#第二次進入時，因為data>self.data所以到else，然後self.right沒有東西