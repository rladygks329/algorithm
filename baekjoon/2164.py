import sys
import _collections
n = int(sys.stdin.readline())

q = _collections.deque([i for i in range(1,n+1)])
last = 0

while q:
    last = q.popleft()
    if q:
        last = q.popleft()
        q.append(last)
print(last)