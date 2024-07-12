from queue import Queue

q = Queue()

q.put("Grape")
print("成功插入 Grape")
q.put("Mango")
print("成功插入 Mango")
q.put("Apple")
print("成功插入 Apple")
print("Queue的長度是 ",q.qsize())
#python可以用qsize