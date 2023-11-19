import sys
n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
visit = [[False] * m for i in range(n)]

cheese = 0
time = 0
s1 = [(0, 0)]
s2 = []

while s1:
    x, y = s1.pop()

    for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        n_x = x + a
        n_y = y + b
        if 0 <= n_x < n and 0 <= n_y < m:
            if visit[n_x][n_y]:
                continue
            if graph[n_x][n_y] == 1 and graph[x][y] == 0:
                visit[n_x][n_y] = True
                s2.append((n_x, n_y))
            elif graph[n_x][n_y] == 0:
                visit[n_x][n_y] = True
                s1.append((n_x, n_y))
    if not s1 and s2:
        time += 1
        cheese = len(s2)
        for a, b in s2:
            graph[a][b] = 0
        s1 = s2
        s2 = []
print(time)
print(cheese)
