import sys
from heapq import heappop, heappush
from collections import deque

# get INPUT
n = int(sys.stdin.readline())
bus = int(sys.stdin.readline())
graph = [[] for i in range(n + 1)]

for _ in range(bus):
    s, e, w = map(int, sys.stdin.readline().split())
    heappush(graph[s], (w, e))

start, destination = map(int, sys.stdin.readline().split())

# solve
INF = n*100000+1
distance = [INF for i in range(n + 1)]
distance[start] = 0

s = [(0, start)]
d = {start: -1}

while s:
    dis, cur = heappop(s)
    for w, e in graph[cur]:
        if distance[e] > distance[cur] + w:
            distance[e] = distance[cur] + w
            d[e] = cur
            s.append((w, e))
# print(distance)
# print(d)
x = destination
load = deque()

while x != -1:
    load.appendleft(x)
    x = d[x]

print(distance[destination])
print(len(load))
print(" ".join(map(str, load)))
'''
다잌스트라 알고리즘
현재 트리에서 가장 비용이 낮은 줄기를 찾아서 거리갱신
다른 노드로 가는 가장 적은 거리를 갱신
'''
