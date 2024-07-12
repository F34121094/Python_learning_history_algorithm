import time
def recur(i):
    print(i,end = "\t")
    time.sleep(1)
    if (i <= 1): return 0
    else: return recur(i-1)

recur(5)