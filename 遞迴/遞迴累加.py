def sum(n):
    if (n <= 1):
        return 1
    else:
        return n + sum(n-1)
print(f"total (5) = {sum(5)}")