import sys

n = int(sys.stdin.readline())

dp = [[float("inf"), float("inf"), float("inf")] for i in range(n+1)]
dp[0] = [0, 0, 0]

for i in range(1, n + 1):
    r, g, b = map(int, sys.stdin.readline().split())
    dp[i][0] = min(dp[i-1][1] + r, dp[i-1][2] + r)
    dp[i][1] = min(dp[i-1][0] + g, dp[i-1][2] + g)
    dp[i][2] = min(dp[i-1][0] + b, dp[i-1][1] + b)

print(min(dp[n]))


