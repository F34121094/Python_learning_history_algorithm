class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Link_list():
    def __init__(self):
        self.head = None

    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

Link_list.head = Node(5)
n2 = Node(15)
n3 = Node(5)
n2.next = n3
Link_list().head.next = n2
n2.next = n3
print("所建立的鏈結串列")
Link_list.print_list()
