import random

def quick_sort(nLst):
    if len(nLst) <= 1:
        return nLst
    left = []
    right = []
    piv = []
    pivot = random.choice(nLst)
    for val in nLst:
        if val == pivot:
            piv.append(val)
        elif val < pivot:
            left.append(val)
        else:
            right.append(val)
    return quick_sort(left) + piv + quick_sort(right)

data = [6,1,5,7,3,9,4,2,8]
print("原始串列 : ", data)
print("排序結果 : " ,quick_sort(data))