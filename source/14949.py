import sys
from collections import deque

height, width = map(int, sys.stdin.readline().split())
graph = []
for i in range(height):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
def find_start():
    for i in range(height):
        for j in range(width):
            if graph[i][j] == 2:
                return i, j


x, y = find_start()
graph[x][y] = 0
q = deque()
q.append((x, y, 0))
visited = [[False for i in range(width)] for j in range(height)]

while q:
    cur_x, cur_y, distance = q.popleft()

    for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= cur_x + a < height and 0 <= cur_y + b < width:
            nxt_x, nxt_y = cur_x + a, cur_y + b
            if visited[nxt_x][nxt_y]:
                continue
            if graph[nxt_x][nxt_y] == 1:
                visited[nxt_x][nxt_y] = True
                graph[nxt_x][nxt_y] = distance + 1
                q.append((nxt_x, nxt_y, distance + 1))

for i in range(height):
    answer = []
    for j in range(width):
        answer.append(graph[i][j] if visited[i][j] else -graph[i][j])
    print(" ".join(map(str, answer)))
