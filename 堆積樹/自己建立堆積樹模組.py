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
        if i*2 + 2 >= self.size:
            return i*2 +1
        else:
            if self.heap[i*2+1] < self.heap[i*2+2]:
                return i*2 + 1
            else:
                return i*2 + 2

    def build_heap(self,mylist):
        i = (len(mylist) // 2) - 1
        self.size = len(mylist)
        self.heap = mylist
        while (i >= 0):
            self.data_down(i)
            i = i - 1

h = [10,21,5,9,13,28,3]b
print("執行前普通串列 = ", h)
obj = Heaptree()
obj.build_heap(h)
print("執行後堆積樹串列 = ",obj.heap)
