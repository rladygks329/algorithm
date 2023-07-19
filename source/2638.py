import sys

n, m = map(int, sys.stdin.readline().split())
graph = list(map(lambda x: list(map(int, x.split())), sys.stdin.read().splitlines()))
visit = [[0 for j in range(m)] for i in range(n)]
count = 0
answer = 0

for i in graph:
    count += i.count(1)

stack = []
stack.append((0, 0))
visit[0][0] = 1

while stack:
    q = stack.copy()
    stack = []

    while q:
        cur_x, cur_y = q.pop()
        for a, b in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= cur_x + a < n and 0 <= cur_y + b < m:
                nxt_x = cur_x + a
                nxt_y = cur_y + b
                if graph[nxt_x][nxt_y] == 0 and visit[nxt_x][nxt_y] == 0:
                    visit[nxt_x][nxt_y] = 1
                    q.append((nxt_x, nxt_y))
                elif graph[nxt_x][nxt_y] == 1 and graph[cur_x][cur_y] == 0:
                    visit[nxt_x][nxt_y] += 1
                    if visit[nxt_x][nxt_y] >= 2:
                        stack.append((nxt_x, nxt_y))
    if stack:
        answer += 1

    for i, j in stack:
        visit[i][j] = 1
        graph[i][j] = 0

print(answer)
