class Heaptree():
    def __init__(self):
        self.heap = []
        self.size = 0
    def data_down(self,i):
        while(i*2 + 2) <= self.size:
            mi = self.get_min_index(i)
            if self.heap[i] > self.heap[mi]:
                self.heap[i], self.heap[mi] = self.heap[mi], self.heap[i]
            i = mi
    def get_min_index(self,i):
        if i * 2 + 2 >= self.size:
            return i*2+1
        else:
            return i*2+2
    def build_heap(self,mylist):
        i = (len(mylist) // 2) - 1
        self.size = len(mylist)
        self.heap = mylist
        while(i >= 0):
            self.data_down(i)
            i -= 1
    def get_min(self):
        min_ret = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heap.pop()
        self.data_down(0)
        return min_ret

data = [10,21,5,9,13,28,3]
print("原始串列 = ", data)
obj = Heaptree()
obj.build_heap(data)

print("執行後堆積樹串列 = ",obj.heap)
sort_h = []
for i in range(len(data)):
    sort_h.append(obj.get_min())
print("排序結果 : ",sort_h)