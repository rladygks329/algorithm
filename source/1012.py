#import sys
#sys.stdin =  open("../input/1012.txt", "r")

import sys
sys.setrecursionlimit(10 ** 4)
num_of_problem = int(sys.stdin.readline())
data = []
valid = []
width, height = 0, 0

def dfs(h, w):
    if(h < 0 or  h > height-1):
        return 0
    if (w < 0 or w > width - 1):
        return 0
    if(data[h][w] == 0):
        return 0
    else:
        data[h][w] = 0
        return 1 + dfs(h, w+1)+ dfs(h, w-1) + dfs(h+1, w) + dfs(h-1, w)

for i in range(num_of_problem):
    width, height, num_of_cabage = map(int, sys.stdin.readline().split())
    cnt = 0
    data = [[0 for j in range(width)] for i in range(height)]

    for j in range(num_of_cabage):
        w, h = map(int, sys.stdin.readline().split())
        data[h][w] = 1
    for h in range(0, height):
        for w in range(0, width):
            if(data[h][w] == 0):
                continue
            dfs(h, w)
            cnt += 1
    print(cnt)

