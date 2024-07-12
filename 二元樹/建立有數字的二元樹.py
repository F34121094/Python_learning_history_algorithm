def creat_btree(tree,data):
    for i in range(len(data)):
        level = 0       #level用來表示第幾層
        if i == 0 :
            tree[level] = data[i]   #當 i 是 0 的時候先把 data[i]的值傳給tree
        else:
            while tree[level]:
                if data[i] > tree[level]:
                    level = level * 2 + 2
                else:
                    level = level * 2 + 1
        tree[level] = data[i]
        print(i,tree)
btree = [0]*8
data = [10,21,5,9,13,28]
creat_btree(btree,data)
for i in range(len(btree)):
    print(f"二元樹[{i}] = {btree[i]}")