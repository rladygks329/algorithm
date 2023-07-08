import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())
num_of_bridge = int(sys.stdin.readline())

graph = [[] for i in range(n + 1)]

for _ in range(num_of_bridge):
    start, end, weight = map(int, sys.stdin.readline().split())
    heappush(graph[start],  (weight, end))

start, end = map(int, sys.stdin.readline().split())

def dijkstra(start, end):
    distance = [float("inf") for i in range(n+1)]
    distance[start] = 0
    s = [(0, start)]

    while s:
        dis, cur = heappop(s)
        for w, nxt in graph[cur]:
            if dis + w < distance[nxt]:
                distance[nxt] = dis + w
                heappush(s, (dis + w, nxt))

    return distance[end]


print(dijkstra(start, end))
