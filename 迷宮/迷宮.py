maze = [
    [1,1,1,1,1,1],
    [1,0,1,0,1,1],
    [1,0,1,0,0,1],
    [1,0,0,0,1,1],
    [1,0,1,0,0,1],
    [1,1,1,1,1,1]
]
direction = [
    lambda x,y: (x-1,y),
    lambda x,y: (x+1,y),
    lambda x,y: (x,y-1),
    lambda x,y: (x,y+1)
]
def maze_solve(x,y,goal_x,goal_y):
    maze[x][y] = 2
    stack = []
    stack.append((x,y))
    print("迷宮開始")
    while (len(stack) > 0):
        cur = stack[-1]
        if cur[0] == goal_x and cur[1] == goal_y:
            print("抵達出口")
            return True
        for dir in direction:
            next = dir(cur[0], cur[1])
            if maze[next[0]][next[1]] == 0:
                stack.append(next)
                maze[next[0]][next[1]] = 2
                break
        else:   #這個else代表for 經過了四個方向沒有找到任何一個方向的數字是0時，進入這個else
            maze[cur[0]][cur[1]] = 3
            stack.pop()
    else:
        print("沒有路徑")
        return False

maze_solve(1,1,4,4)
for i in range(len(maze)):
    print(maze[i])
