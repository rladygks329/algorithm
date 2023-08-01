import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
visit = [False] * 100_001
count = 0

#bfs
q = deque()
q.append((n, 0))
def valid(x):
    if 0 <= x <= 100000 and not visit[x]:
        return True
    return False

def DFS():
    while q:
        cur, time = q.popleft()
        while valid(cur):
            if cur == m:
                print(time)
                return
            q.append((cur - 1, time + 1))
            q.append((cur + 1, time + 1))
            visit[cur] = True
            cur *= 2
DFS()
