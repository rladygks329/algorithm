import sys
from heapq import heappop, heappush

# 2번에서 출발해서 다른 노드까지 도착하는데 걸리는 최솟값을 알아낸다 ( target -> every one)
# 2번에서 출발하고 reverse Node를 사용하여 다른 노드가 도착하는데 걸리는 최솟값을 알아낸다. (everyone -> target)

INF = 1e10
n, m, x = map(int, sys.stdin.readline().split())
_map = [[] for i in range(n)]
_reverse_map = [[] for i in range(n)]

for i in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    start -= 1
    end -= 1
    _map[start].append((end, weight)) # 출발해서 도착까지 걸리는 맵
    _reverse_map[end].append((start, weight)) # 도착지에서 출발지로 가는 맵 즉 역방향!

def dijkstra(s, graph):
    dist = [INF] * n
    dist[s] = 0
    q = []
    heappush(q, (s, 0))

    while q:
        cur_node, cur_dist = heappop(q)

        for next, weight in graph[cur_node]:
            if cur_dist + weight < dist[next]:
                dist[next] = cur_dist + weight
                heappush(q, (next, cur_dist + weight))

    return dist


a = dijkstra(x-1, _map)
b = dijkstra(x-1, _reverse_map)
for i in range(n):
    a[i] += b[i]
print(max(a))
