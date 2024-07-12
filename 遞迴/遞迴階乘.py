def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
value = 3
print(f"{value} 的階乘為 {factorial(value)}")
