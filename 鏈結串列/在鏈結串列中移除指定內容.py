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
    def ending(self, newdata):
        new_node = Node(newdata)
        if self.head == None:
            self.head = new_node
            return
        last_ptr = self.head
        while last_ptr.next:
            last_ptr = last_ptr.next
        last_ptr.next = new_node
    def rm_node(self,rmkey):
        ptr = self.head     # ptr 這時是在指目前的頭
        if ptr:
            if ptr.data == rmkey:   #如果現在的頭就是要移除的那一個
                self.head = ptr.next    #將下一個設為頭
                return          #回去
        while ptr:
            if ptr.data == rmkey:   #不會是第一個，
                break
            prev = ptr  #用prev來記錄ptr的前一個
            ptr = ptr.next
        if ptr == None:     #如果沒有找到ptr的話直接返回
            return
        prev.next = ptr.next    #將ptr的前一個下一個設定為ptr的下個


link = Linked_list()
link.head = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head.next = n2
n2.next = n3
link.print_list()
print("新的鏈結串列")
link.rm_node(15)
link.print_list()