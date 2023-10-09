import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

enter = [0 for i in range(n + 1)]
arr = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split()) # a < b
    enter[b] += 1
    arr[a].append(b)

q = deque()
for i in range(1, n + 1):
    if enter[i] == 0:
        q.append(i)

result = []
while q:
    node = q.popleft()
    result.append(node)
    for n_node in arr[node]:
        enter[n_node] -= 1
        if enter[n_node] == 0:
            q.append(n_node)

print(' '.join(map(str, result)))