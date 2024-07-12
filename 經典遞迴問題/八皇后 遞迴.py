class Queens:
    def __init__(self): #i love you
        self.queens = size * [-1]
        self.solve(0)
        for i in range(size):
            for j in range(size):
                if self.queens[i] == j:
                    print("Q", end = '')
                else:
                    print(".",end = '')
            print()
    def is_OK(self, row , col):
        for i in range(1, row+1):
            if (self.queens[row - i] == col
                or self.queens[row - i] == col - i
                or self.queens[row - i] == col + i):
                return False
        return True

    def solve(self, row):
        if row == size:
            return True
        for col in range(size):
            self.queens[row] = col
            if self.is_OK(row, col) and self.solve(row + 1):
                return True
        return False

size = 8
Queens()