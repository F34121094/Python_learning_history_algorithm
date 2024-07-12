def selection_sort(nLst):
    for i in range(len(nLst) - 1):
        index = i
        for j in range(i+1, len(nLst)):
            if nLst[index] > nLst[j]:
                index = j
        if i == index:
            pass
        else:
            nLst[i],nLst[index] = nLst[index],nLst[i]
        print(f"第 {i+1} 次迴圈排序 {nLst}")
    return nLst

data = [6,1,5,7,3]
print("原始排序 : ",data)
print("排序過後 : ",selection_sort(data))