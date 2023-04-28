import sys
import math
from collections import deque
n = int(sys.stdin.readline())

def solve(n):
    q = deque()
    q.append((n, 0))

    while q:
        cur, length = q.popleft()
        for i in range(int(math.sqrt(cur))+1, 0, -1):
            if cur - i*i == 0 and length < 4:
                print(length + 1)
                return
            elif cur - i*i > 0 and length < 4:
                q.append((cur-i*i, length + 1))
solve(n)
# bfs로 푼다고 하면
# 1번 노드를 방문 count = 1
# n - i*i >= 0
