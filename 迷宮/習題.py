maze = [
    [1,1,1,1,1,1],
    [1,0,1,0,1,1],
    [1,0,1,0,0,1],
    [1,0,0,0,1,1],
    [1,0,1,0,0,1],
    [1,1,1,1,1,1]
]
direction = [
    lambda x,y : (x-1,y),
    lambda x,y : (x+1,y),
    lambda x,y : (x,y-1),
    lambda x,y : (x,y+1),
]
def solve(x,y,goal_x,goal_y):
    print("迷宮開始")
    stack = []
    stack.append((x,y))
    maze[x][y] = 2
    while len(stack) > 0:
        current = stack[-1]
        if current[0] == goal_x and current[1] == goal_y:
            maze[current[0]][current[1]] = 8
            print(f"目前位置 : {current}")
            print("抵達出口")
            return True

        for dir in direction:
            next = dir(current[0],current[1])
            if maze[next[0]][next[1]] == 0:
                print(f"目前位置 : {current}")
                stack.append(next)
                maze[next[0]][next[1]] = 2
                break
        else:
            maze[current[0]][current[1]] = 3
            stack.pop()
    else:
        print("迷宮沒有解")

for i in range(len(maze)):
    print(maze[i])

x,y = input("請輸入起點 x,y : ").split()
goal_x,goal_y = input("請輸入終點 x,y : ").split()
x, y, goal_x, goal_y = int(x),int(y),int(goal_x),int(goal_y)
solve(x,y,goal_x,goal_y)
for i in range(len(maze)):
    print(maze[i])