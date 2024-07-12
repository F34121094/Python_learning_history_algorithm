def cocktail_sort(nLst):
    n = len(nLst)
    is_sorted = True
    start = 0
    end = n - 1
    while is_sorted:
        is_sorted = False
        for i in range(start, end):
            if (nLst[i] > nLst[i+1]):
                nLst[i], nLst[i + 1] = nLst[i + 1], nLst[i]
                is_sorted = True
        print("往後排序過程 : ",nLst)
        if not is_sorted:
            break

        end -= 1
        for i in range(end-1, start-1, -1):
            if (nLst[i] > nLst[i + 1]):
                nLst[i], nLst[i + 1] = nLst[i + 1], nLst[i]
                is_sorted = True
            print("往前排序過程 : ",nLst)
    return nLst

data = [6,1,5,7,3,14,16,7,2,76,45]
print("原始串列 : ", data)
print("排序過後 : ", cocktail_sort(data))