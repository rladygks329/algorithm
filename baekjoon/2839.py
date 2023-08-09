import sys

n = int(sys.stdin.readline())
#dp[n]은 n까지 가는 최소 값
dp = [2000 for i in range(n+1)]
dp[3] = 1
if (n >= 5):
    dp[5] = 1
for i in range(6, n + 1):
    if (dp[i - 3] > 1999 and dp[i - 5] > 1999):
        continue
    dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)
print(-1 if (dp[n] > 1999) else dp[n])

for i in range(n+1):
    print(i," ", dp[i])