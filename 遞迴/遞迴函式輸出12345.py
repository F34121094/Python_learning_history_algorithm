import time
def recur(i):
    if i <= 0: return 0
    else:
        recur(i-1)
    print(i,end = "\t")

recur(5)