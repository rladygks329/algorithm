import sys

n, limit = map(int, sys.stdin.readline().split())
dp = [[0] * (limit + 1) for i in range(n + 1)]
arr = [(0, 0)]

for _ in range(n):
    weight, value = map(int, sys.stdin.readline().split())
    arr.append((weight, value))

for i in range(1, n+1):
    cur_weight = arr[i][0]
    cur_value = arr[i][1]

    for j in range(1, limit+1):
        if j - cur_weight >= 0:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-cur_weight] + cur_value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])
'''
        0 1 2 3 4 5 6 7
        0 0 0 0 0 0 0 0
6 13    0 0 0 0 0 0 13 13
4 8     0 0 0 0 8 8 13 13
3 6     0 0 0 6 8 8 13 14
5 12    0 0 0 6 8 12 13 14
'''
