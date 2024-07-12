def select(list):
    for i in range(len(list)-1):
        index =  i
        for j in range(index + 1,len(list)):
            if list[index][2] < list[j][2]:
                index = j
        if i == index:
            pass
        else:
            list[i],list[index] = list[index],list[i]
    return list
rank = [
    ("李宗盛","山丘",24740000),
    ("趙傳","我是一隻小小鳥",8310000),
    ("五百","挪威的森林",34130000),
    ("林憶蓮","聽說愛情回來過",12710000)
]
print("Youtube 點播排行")
select(rank)
for i in range(len(rank)):
    print(f"{i+1}, {rank[i][0]}{rank[i][1]} --- 點播次數 {rank[i][2]}")