import sys

n = int(sys.stdin.readline())
triangle = []
answer = 0
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))



for i in range(1, n):
    for j in range(i + 1):
        tmp = []
        if j - 1 >= 0:
            tmp.append(triangle[i-1][j-1])
        if j < i:
            tmp.append(triangle[i-1][j])

        triangle[i][j] += max(tmp)

print(max(triangle[n-1]))
