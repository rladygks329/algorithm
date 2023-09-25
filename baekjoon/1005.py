import sys
from collections import deque

class Node:
    def __init__(self, val, buildTime):
        self.val = val
        self.buildTime = buildTime
        self.next = []

T = int(sys.stdin.readline())
for _ in range(T):
    num_of_buildings, num_of_building_rule = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().strip().split()))
    nodes = [Node(i, time[i]) for i in range(num_of_buildings)]
    isLeaf = [True] * num_of_buildings

    for __ in range(num_of_building_rule):
        x, y = map(int, sys.stdin.readline().split())
        x -= 1
        y -= 1
        isLeaf[y] = False
        nodes[x].next.append(y)

    target = int(sys.stdin.readline())
    target -= 1

    distances = [-1] * num_of_buildings
    q = deque()
    answer = -1

    for i in range(num_of_buildings):
        if isLeaf[i]:
            q.append((time[i], nodes[i]))

    while q:
        dis, node = q.popleft()
        if dis < distances[node.val]:
            continue
        if node.val == target:
            answer = max(answer, dis)
            continue
        for n in node.next:
            if distances[n] < dis + time[n]:
                distances[n] = dis + time[n]
                q.append((dis + time[n], nodes[n]))
    print(answer)
