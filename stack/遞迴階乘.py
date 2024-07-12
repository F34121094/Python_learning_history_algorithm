def factorial(n):
    global fact
    #global 是在你需要在函式修改你的變數值時用的
    if n == 1:
        print(f"factorial ({n}) 呼叫前 {n} != {fact}")
        print("到達遞迴條件終止 n = 1")
        fact = 1
        print(f"factorial ({n}) 返回後 {n} != {fact}")
        return fact
    else:
        print(f"factorial ({n}) 呼叫前 {n} != {fact}")
        fact = n*factorial(n-1)
        print(f"factorial ({n}) 返回後 {n} != {fact}")
        return fact

fact = 0
N = eval(input("請輸入階乘數 : "))
print(f"{N} 的階乘結果為 = {factorial(N)}")