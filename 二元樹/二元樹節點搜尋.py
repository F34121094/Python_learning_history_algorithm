class Node():
    def __init__(self,data = None):
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
    def search(self,val):
        if val < self.data:     #如果輸入的val比根節點小
            if not self.left:       #如果沒有左子節點
                return str(val) + " not exist"
            return self.left.search(val)    #用該子節點繼續找
        elif val > self.data:
            if not self.right:
                return str(val) + " not exist"
            return self.right.search(val)
        else:
            return str(val) + " found!"     #代表val == self.data代表找到

tree = Node()
datas = [10,21,5,9,13,28]
for d in datas:
    tree.insert(d)

n = eval(input("請輸入欲搜尋資料 : "))
print(tree.search(n))