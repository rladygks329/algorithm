import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
tp = [0 for i in range(101)]

for i in range(n + m):
    a, b = map(int, sys.stdin.readline().split())
    tp[a] = b

#BFS
q = deque([(1, 0)])
visit = [0 for i in range(101)]

while q:
    cur, step = q.popleft()
    if cur == 100:
        print(step)
        sys.exit()

    for i in range(1, 7):
        if cur+i <= 100 and visit[cur + i] == 0:
            if tp[cur+i] == 0:
                visit[cur+i] = step + 1
                q.append((cur+i, step + 1))
            else:
                visit[cur+i] = step
                q.append((tp[cur+i], step + 1))
