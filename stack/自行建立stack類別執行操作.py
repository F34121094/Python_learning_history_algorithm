class Stack():
    def __init__(self):
        self.my_stack = []
        #__init__在定義這個class裡面有甚麼東西
    def my_push(self,data):
        self.my_stack.append(data)
        #定義在class裡面的def在定義這個class可以用的功能，可以使用之前在__init__中定義的變數
    def my_pop(self):
        return self.my_stack.pop()
    def size(self):
        return len(self.my_stack)

stack = Stack()
fruits = ['Grape','Mango','Apple']
for fruit in fruits:
    stack.my_push(fruit)
    print(f'將 {fruit} 水果堆入堆疊')

print(f"堆疊有 {stack.size()} 種水果")