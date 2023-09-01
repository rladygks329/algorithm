import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]
houses = []
chickens = []

# init
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))

answer = 1000000
for remained_chicken in combinations(chickens, m):
    distance = 0
    for house in houses:
        distances = [abs(house[0] - i[0]) + abs(house[1] - i[1]) for i in remained_chicken]
        distance += min(distances)
    answer = min(answer, distance)
print(answer)