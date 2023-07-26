import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = 1_000_000_000
distance = [[0 if i == j else INF for i in range(n)] for j in range(n)]

def solve():
    for i in range(n):
        for j in range(n):
            for k in range(n):
                distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])
#in
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    distance[a-1][b-1] = min(c, distance[a-1][b-1])

solve()

for i in range(n):
    for j in range(n):
        print(0 if distance[i][j] >= INF else distance[i][j], end=" ")
    print()
