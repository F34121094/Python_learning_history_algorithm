class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

n1 = Node(5)
n2 = Node(15)
n3 = Node(25)
n1.next = n2
n2.next = n3
n3.next = n1
ptr = n1
counter = 1
while counter <= 6:
    print(ptr.data)
    ptr = ptr.next
    counter += 1