import sys
from collections import deque

n, target = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

q = deque([i for i in range(1, n+1)])
ans = 0

for target in data:
    left = q.index(target)
    right = len(q) - 1 - left

    while q[0] != target:
        if left <= right:
            q.append(q.popleft())
        else:
            q.appendleft(q.pop())
        ans += 1
    q.popleft()
print(ans)
