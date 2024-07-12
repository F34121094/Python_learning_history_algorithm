def hanoi(n,src,aux,dst):   #src 是 來源， aux 是 輔助， dst 是 目標
    global step
    if n == 1:
        step += 1
        print(f"{step:2d} : 移動圓盤 {n} 從 {src} 到 {dst}")
    else:
        hanoi(n-1,src,dst,aux)
        step += 1
        print(f"{step:2d} : 移動圓盤 {n} 從 {src} 到 {dst}")
        hanoi(n-1,aux,src,dst)

step = 0
n = int(input("請輸入圓盤數量 : "))
hanoi(n,"A","B","C")