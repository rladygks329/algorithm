import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[0] * n for i in range(n)]
arr = []

apples = int(sys.stdin.readline())
for i in range(apples):
    x, y = map(int, sys.stdin.readline().strip().split())
    x -= 1
    y -= 1
    graph[x][y] = 3

changeDir = int(sys.stdin.readline())
for i in range(changeDir):
    time, dir = sys.stdin.readline().strip().split()
    arr.append((int(time), dir))

index = 0
dir = "R"
dir_add = {
    "R": [0, 1],
    "L": [0, -1],
    "U": [-1, 0],
    "D": [1, 0]
}
L = {
    "R": "U",
    "L": "D",
    "U": "L",
    "D": "R"
}
D = {
    "R": "D",
    "L": "U",
    "U": "R",
    "D": "L"
}
isAlive = True
h, w = 0, 0
answer = 0
q = deque([(0, 0)])
graph[0][0] = 1

while isAlive:
    a, b = dir_add[dir]
    if 0 <= h + a < n and 0 <= w + b < n:
        h += a
        w += b
        if graph[h][w] == 1:
            break
        if graph[h][w] == 0:
            rm_h, rm_w = q.popleft()
            graph[rm_h][rm_w] = 0
        q.append((h, w))
        graph[h][w] = 1
    else:
        break
    answer += 1
    if index < len(arr) and answer == arr[index][0]:
        dir = L[dir] if arr[index][1] == "L" else D[dir]
        index += 1

print(answer + 1)