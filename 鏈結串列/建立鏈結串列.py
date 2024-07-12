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

link = Linked_list()
link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head.next = n2
n2.next = n3
link.print_list()