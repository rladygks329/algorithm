import sys
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dis = [float("inf") for i in range(n + 1)]
dis[start] = 0
q = [(0, start)]

while q:
    distance, node,  = heappop(q)

    for next, weight in graph[node]:
        if dis[next] > distance + weight:
            dis[next] = distance + weight
            heappush(q, (distance + weight, next))

for i in range(1, n + 1):
    print("INF" if dis[i] == float("inf") else dis[i])
