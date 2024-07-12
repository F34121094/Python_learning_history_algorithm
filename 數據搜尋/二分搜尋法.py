def binary_search(nLst):
    print("列印搜尋串列 : ",nLst)
    low = 0
    high = len(nLst) - 1
    middle = (low + high)//2
    times = 0
    while 1:
        times += 1
        if key == nLst[middle]:
            rtn = middle
            break
        elif key > nLst[middle]:
            low = middle + 1
        else:
            high = middle - 1
        middle = (high + low) // 2
        if low > high:
            rtn = -1
            break
    return rtn, times

data = [19,32,28,99,10,88,62,8,6,3]
sorted_data = sorted(data)
key = eval(input("清輸入搜尋值 : "))
index, times = binary_search(sorted_data)
if index != -1:
    print(f"在索引 {index} 位置找到了，共找了 {times} 次")
else:
    print("查無此搜尋號碼")