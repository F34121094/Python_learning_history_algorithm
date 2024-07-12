def merge(left, right):
    output = []
    while left and right:
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    if left:
        output += left
    if right:
        output += right
    return output

def merge_sort(nLst):
    if len(nLst) <= 1:
        return nLst
    mid = len(nLst) // 2
    left = nLst[:mid]
    right = nLst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)

data = [6,1,5,7,3,9,4]
print("原始串列 : ",data)
print("排序結果 : ", merge_sort(data))