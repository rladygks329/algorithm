import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[[0] * 3 for j in range(n)] for i in range(n)]
dp[0][1][0] = 1

for i in range(2, 2 * n - 1):
    for j in range(n):
        for k in range(n):
            if j + k != i or graph[j][k] == 1:
                continue
            #가로 방향
            dp[j][k][0] += dp[j][k - 1][0]
            dp[j][k][0] += dp[j][k - 1][2]

            #세로 방향
            dp[j][k][1] += dp[j - 1][k][1]
            dp[j][k][1] += dp[j - 1][k][2]

            if graph[j-1][k] == 1 or graph[j][k-1] == 1:
                continue
            #대각선 방향
            dp[j][k][2] += dp[j - 1][k - 1][0]
            dp[j][k][2] += dp[j - 1][k - 1][1]
            dp[j][k][2] += dp[j - 1][k - 1][2]

print(sum(dp[n-1][n-1]))
