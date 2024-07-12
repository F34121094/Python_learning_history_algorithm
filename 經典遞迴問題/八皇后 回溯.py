def is_OK(row, col):
    for i in range(1, row+1):
        if (queens[row - i] == col
            or queens[row-i] == col - i
            or queens[row-i] == col + i):
            return False
    return True

def location(row):
    start = queens[row] + 1
    for col in range(start, SIZE):
        if is_OK(row, col):
            return col
    return -1

def solve():
    row = 0
    while row >= 0 and row <= 7:    #會一直在這裡面 直到不符合條件
        col = location(row)
        if col < 0:
            queens[row] = -1
            row -= 1
        else:
            queens[row] = col
            row += 1    #row +1 代表queens放置的位置移動到下一行
    if row == -1:
        return False
    else:
        return True #return True代表所有的棋都被放置到了對的位置

SIZE = 8    #定義了8*8棋盤
queens = [-1] * SIZE    #設定一個長度為8的列
#queens 是用來記錄 每一行的皇后站在哪(第一個站在索引 0 的位置)
solve()     #進入solve()函式
for i in range(SIZE):
    for j in range(SIZE):
        if queens[i] == j:
            print("Q", end="")
        else:
            print(".", end = "")
    print()


