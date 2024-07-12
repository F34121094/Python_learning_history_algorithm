class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.insert(0,data)

    def size(self):
        return len(self.queue)

q= Queue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
print("Queue 的長度是 : ",q.size())