from collections import deque
#deque是一個雙端對列，允許元素從兩端被填入、刪除

graph = {}
#建立一個graph字典
graph['Tom'] = ['Ivan','Ira','Kevin']
#這一行表示Tom的朋友列表有([那三個人])
people = deque()
#建立一個空的deque(雙向串列)
people += graph['Tom']
#利用+=將Tom打印到people中
print("列出people資料類型 : ", type(people))
print("列出搜尋名單       : ", people)
for name in range(len(people)):
    print(people.popleft())

#appendleft()可以從左邊加入元素
#popleft()可以從左邊刪除元素
