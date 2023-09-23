import sys

r, c, t = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(r)]
air_conditions = []

for i in range(r):
    if graph[i][0] == -1:
        air_conditions.append(i)
def spread():
    arr = [[0] * c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] in [0, -1]:
                continue
            arr[i][j] += graph[i][j]
            if graph[i][j] < 5:
                continue
            tmp = []
            for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= i + a < r and 0 <= j + b < c:
                    if graph[i+a][j+b] != -1:
                        tmp.append((i + a, j + b))
            add = graph[i][j] // 5
            for a, b in tmp:
                arr[a][b] += add
                arr[i][j] -= add
    return arr


def clean():
    up = air_conditions[0]
    down = air_conditions[1]

    # up
    for i in range(up, -1, -1):
        graph[i][0] = graph[i - 1][0]
    for i in range(c - 1):
        graph[0][i] = graph[0][i + 1]
    for i in range(up):
        graph[i][c-1] = graph[i + 1][c - 1]
    for i in range(c - 1, 0, -1):
        graph[up][i] = graph[up][i-1]


    # down
    for i in range(down, r - 1):
        graph[i][0] = graph[i + 1][0]
    for i in range(c - 1):
        graph[r-1][i] = graph[r-1][i + 1]
    for i in range(r - 1, down, -1):
        graph[i][c - 1] = graph[i - 1][c - 1]
    for i in range(c - 1, 0, -1):
        graph[down][i] = graph[down][i - 1]

    graph[up][0] = -1
    graph[down][0] = -1

    graph[up][1] = 0
    graph[down][1] = 0
    return


for _ in range(t):
    graph = spread()
    clean()

answer = 0
for i in graph:
    answer += sum(i)

print(answer + 2)