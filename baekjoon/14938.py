import sys

INF = 1000_000_000
n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
_graph = [[INF] * n for i in range(n)]

for _ in range(r):
    a, b, length = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    _graph[a][b] = length
    _graph[b][a] = length

# Bellman - Ford
for i in range(n):
    for j in range(n):
        for k in range(n):
            # max loop: 100 x 100 x 100 => 1000000
            _graph[i][k] = min(_graph[i][k], _graph[i][j] + _graph[j][k])

answer = 0
for i in range(n):
    visited = [False] * n
    tmp = items[i]

    s = [(0, i)]
    visited[i] = True
    while s:
        dis, node = s.pop()
        for j in range(n):
            if not visited[j] and dis + _graph[node][j] <= m:
                tmp += items[j]
                visited[j] = True
                s.append([dis + _graph[node][j], j])
    answer = max(answer, tmp)
print(answer)
