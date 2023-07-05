import sys

n, m = map(int, sys.stdin.readline().split())
graph = sys.stdin.read().splitlines()

x, y = 0, 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            x, y = i, j

answer = 0
visited = [[False for i in range(m)] for j in range(n)]
visited[x][y] = True
s = [(x, y)]

while s:
    cur_x, cur_y = s.pop()

    for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nxt_x, nxt_y = cur_x + a, cur_y + b
        if 0 < nxt_x <= n or nxt_y < 0:
            continue
        if nxt_x >= n or nxt_y >= m:
            continue
        if visited[cur_x + a][cur_y + b]:
            continue

        if graph[cur_x + a][cur_y + b] == "P":
            answer += 1
            visited[cur_x + a][cur_y + b] = True
            s.append((cur_x + a, cur_y + b))
        elif graph[cur_x + a][cur_y + b]  == "O":
            visited[cur_x + a][cur_y + b] = True
            s.append((cur_x + a, cur_y + b))

print( "TT" if answer == 0 else answer)
