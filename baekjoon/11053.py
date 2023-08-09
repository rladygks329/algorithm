import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for i in range(n)]
dp[0] = 1

for i in range(1, n):
    tmp = 1
    for j in range(i):
        if arr[j] < arr[i]:
            tmp = max(tmp, dp[j] + 1)
    dp[i] = tmp

#print(dp)
print(max(dp))

