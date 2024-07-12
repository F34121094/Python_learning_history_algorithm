def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)

n = int(input("請輸入你的費氏數列的要算到多少 : "))
for i in range(n+1):
    print(f"n = {i}, F({i}) = {F(i)}")
