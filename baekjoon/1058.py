import sys
from collections import deque

n = int(sys.stdin.readline())
_map = sys.stdin.read().splitlines()
ans = 0

for i in range(n):

    visit = [False] * n
    visit[i] = True
    count = 0
    q = deque([i])
    step = 0
    size = 1
    while q and step < 2:
        node = q.popleft()
        for j in range(n):
            if visit[j]:
                continue
            if _map[node][j] == "Y":
                count += 1
                visit[j] = True
                q.append(j)
        size -= 1
        if size == 0:
            step += 1
            size = len(q)
    ans = max(ans, count)

print(ans)
