from queue import Queue

q = Queue()

q.put("漢堡")
print("成功插入 漢堡")
q.put("薯條")
print("成功插入 薯條")
q.put("可樂")
print("成功插入 可樂")
print("輸出:")
while q:
    print(q.get())

#python可以用qsize