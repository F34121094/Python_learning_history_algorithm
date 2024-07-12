class Node():
    #這裡在建立鏈結串列的規則
    def __init__(self,data = None):
        self.data = data    #這個在建立內容
        self.next = None    #這個在建立指標
class Linked_list():
    def __init__(self):
        self.head = None
        #設定第一個
    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    def between(self, pre_node, newdata):
        if pre_node == None:        #如果插入的前一個沒有結點(節點是空的)
            print("缺插入節點的前一個節點")    #就輸出他前面沒有節點
            return
        new_node = Node(newdata)
        new_node.next = pre_node.next
        pre_node.next = new_node

link = Linked_list()
link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head.next = n2
n2.next = n3
link.print_list()
print("新的鏈結串列")
link.between(n2,100)
link.print_list()