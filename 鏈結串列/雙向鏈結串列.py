class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.previous = None

class Double_linked_list():
    def __init__(self):
        self.head = None    #定義一個頭
        self.tail = None    #再定義一個尾

    def add_double_list(self, new_node):
        if isinstance(new_node, Node):  #isinstance()是檢查類別
            if self.head == None:       #如果現在還沒有定義他的頭是啥，進入這個迴圈
                self.head = new_node    #頭是這個新的new_node
                new_node.previous = None    #設定他的previous沒有東西
                new_node.next = None    #他的next也無
                self.tail = new_node    #尾巴也設定
            else:       #如果這個不是頭
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
        return
    def print_list_from_head(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
    def print_list_from_tail(self):
        ptr = self.tail
        while ptr:
            print(ptr.data)
            ptr = ptr.previous
double_link = Double_linked_list
n1 = Node(5)
n2 = Node(15)
n3 = Node(25)

for n in [n1,n2,n3]:
    double_link.add_double_list(n)
    print("從頭部列印雙向鏈結串列")
    double_link.print_list_from_head()

print("從尾部列印雙向鏈結串列")
double_link.print_list_from_tail()