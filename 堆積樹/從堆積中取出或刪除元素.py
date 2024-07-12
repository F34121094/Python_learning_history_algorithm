import heapq
h = [10,21,5,9,13,28,3]
heapq.heapify(h)

print("取出前 h = ",h)
val = heapq.heappop(h)
#取出會取出最小值
print("取出元素 = ",val)
print("取出後 h = ",h)