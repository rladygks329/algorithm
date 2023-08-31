import copy
import sys
from itertools import combinations
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
empty = []
virus = []

def dfs():
    test_map = copy.deepcopy(graph)
    q = deque(copy.deepcopy(virus))
    while q:
        x, y = q.popleft()

        for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nxt_x = x + a
            nxt_y = y + b
            if nxt_x < 0 or nxt_y < 0 or nxt_x >= n or nxt_y >= m:
                continue
            if test_map[nxt_x][nxt_y] != 0:
                continue
            test_map[nxt_x][nxt_y] = 2
            q.append((nxt_x, nxt_y))

    result = 0
    for i in range(n):
        for j in range(m):
            if test_map[i][j] == 0:
                result += 1

    return result


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

answer = 0
for walls in combinations(empty, 3):
    for x, y in walls:
        graph[x][y] = 1
    answer = max(answer, dfs())
    for x, y in walls:
        graph[x][y] = 0

print(answer)