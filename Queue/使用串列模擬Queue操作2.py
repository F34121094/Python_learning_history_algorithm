class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self,data):
        self.queue.insert(0,data)
    def dequeue(self):
        if len(self.queue):
            return self.queue.pop()
        return "Queue是空的"

q = Queue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
print("讀取1 : ",q.dequeue())
print("讀取2 : ",q.dequeue())
print("讀取3 : ",q.dequeue())
print("讀取4 : ",q.dequeue())