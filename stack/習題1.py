class Stack():
    def __init__(self):
        self.stack = []
    def put(self,data):
        for i in range(len(data)):
            self.stack.append(data[i])
            print(f"將 {data[i]} 放入堆疊中")
    def len(self):
        print(f"堆疊有 {len(self.stack)} 種水果")
    def get(self):
        for i in range(len(self.stack)):
            print(f"從堆疊中取出 {self.stack[-1]} ，並且不刪除")
    def print(self):
        while self.stack:
            print(self.stack.pop())
s = Stack()
fruits = ['Grape','Mango','Apple']
s.put(fruits)
s.len()
s.get()
s.print()