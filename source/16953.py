import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
# b to a
q = deque([(b, 0)])
answer = 0
visit = set()

while q:
    num, count = q.popleft()
    if num == a:
        answer = count + 1
        break
    if num%2 == 0:
        nxt = num//2
        if nxt not in visit:
            visit.add(nxt)
            q.append((nxt, count + 1))
    elif num%10 == 1:
        nxt = num//10
        if nxt not in visit:
            visit.add(nxt)
            q.append((nxt, count + 1))

print(-1 if answer == 0 else answer)
