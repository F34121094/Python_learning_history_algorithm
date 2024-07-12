def solve(n,a,b,c):
    solve(n-1, a,)
    print(f"將圓盤 {n} 從 {a} 移動到 {c}")
    solve(n-1)
n = int(input("請輸入圓盤數量 : "))
solve(n, "A","B","C")
