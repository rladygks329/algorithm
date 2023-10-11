import sys
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().strip().split())
arr = [[] for i in range(n + 1)]
count = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    count[b] += 1
    arr[a].append(b)

answer = []
h = []
for i in range(1, n+1):
    if count[i] == 0:
        heappush(h, i)

while h:
    node = heappop(h)
    answer.append(node)
    for x in arr[node]:
        count[x] -= 1
        if count[x] == 0:
            heappush(h, x)

print(' '.join(map(str, answer)))
