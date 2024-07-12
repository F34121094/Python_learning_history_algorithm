def insert_sort(nLst):
    n = len(nLst)
    if n == 1:
        print(f"第 {n} 次迴圈排序 {nLst}")
        return nLst
    print("第 1 次迴圈排序", nLst)
    for i in range(1,n):
        for j in range(i,0,-1):
            if nLst[j] < nLst[j-1]:
                nLst[j],nLst[j - 1] = nLst[j-1],nLst[j]
            else:
                break
        print(f"第 {n+1} 次迴圈排序 {nLst}")
    return nLst

data =[6,1,5,7,5]
print("原始排序 : ", data)
print("排序過後 : ", insert_sort(data))