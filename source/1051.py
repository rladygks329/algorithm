import sys

n, m = map(int, sys.stdin.readline().split())
arr = sys.stdin.read().splitlines()

limit = max(m, m)
ans = 0
for i in range(n):
    for j in range(m):
        cur = arr[i][j]
        for k in range(limit):
            if i+k >= n or j+k >= m:
                continue
            if cur != arr[i + k][j]:
                continue
            if cur != arr[i][j + k]:
                continue
            if cur != arr[i + k][j + k]:
                continue
            ans = max(k+1, ans)
print(ans**2)
