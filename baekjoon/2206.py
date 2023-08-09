import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

stdin = sys.stdin.read().splitlines()

MAX_DISTANCE = (n * m) + 1
graph = [[int(i) for i in j] for j in stdin]
visit = [[False for i in range(m)] for j in range(n)]
visit_with_break = [[False for i in range(m)] for j in range(n)]
answer = [[MAX_DISTANCE for i in range(m)] for j in range(n)]

q = deque()
q.append([0, 0, True, 1]) # x, y, can break, distance
visit[0][0] = True
answer[0][0] = 1

while q:
    x, y, breakable, distance = q.popleft()

    for a, b in [[1, 0], [-1, 0],[0, 1], [0, -1]]:
        if 0 <= x + a < n and 0 <= y + b < m:
            nxt_x = x + a
            nxt_y = y + b

            if breakable:
                if visit[nxt_x][nxt_y]:
                    continue
                if graph[nxt_x][nxt_y] == 1 and breakable:
                    visit[nxt_x][nxt_y] = True
                    answer[nxt_x][nxt_y] = min(answer[nxt_x][nxt_y], distance + 1)
                    q.append([nxt_x, nxt_y, False, distance + 1])
                elif graph[nxt_x][nxt_y] == 0:
                    visit[nxt_x][nxt_y] = True
                    answer[nxt_x][nxt_y] = min(answer[nxt_x][nxt_y], distance + 1)
                    q.append([nxt_x, nxt_y, breakable, distance + 1])
            else:
                if visit_with_break[nxt_x][nxt_y]:
                    continue
                if graph[nxt_x][nxt_y] == 0:
                    visit_with_break[nxt_x][nxt_y] = True
                    answer[nxt_x][nxt_y] = min(answer[nxt_x][nxt_y], distance + 1)
                    q.append([nxt_x, nxt_y, breakable, distance + 1])


print(-1 if answer[n-1][m-1] == MAX_DISTANCE else answer[n-1][m-1])
