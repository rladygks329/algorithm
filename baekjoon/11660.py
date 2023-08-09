import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[0] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(1, n+1):
        arr[i][j] = line[j-1]

for i in range(1, n+1):
    for j in range(1, n+1):
        arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1]
    print(answer)
