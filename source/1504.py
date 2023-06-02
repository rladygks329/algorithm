import sys
from heapq import heappop, heappush

N, E = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

waypoint1, waypoint2 = map(int, sys.stdin.readline().split())


def helper(s):
    distance = [float("inf") for i in range(N + 1)]
    distance[s] = 0
    q = []
    heappush(q, [distance[s], s])

    while q:
        cur_distance, cur_destination = heappop(q)
        if distance[cur_destination] < cur_distance:
            continue

        for a, b in graph[cur_destination]:
            next_dis = cur_distance + b
            if next_dis < distance[a]:
                distance[a] = next_dis
                heappush(q, [next_dis, a])
    return distance

dis1 = helper(1)
dis2 = helper(N)
dis3 = helper(waypoint1)

answer = min(dis1[waypoint1] + dis2[waypoint2], dis1[waypoint2] + dis2[waypoint1]) + dis3[waypoint2]
print(-1 if answer == float("inf") else answer)