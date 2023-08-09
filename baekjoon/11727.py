import sys

n = int(sys.stdin.readline())
dp = [1, 3, 5]

for i in range(2, n):
    dp.append(dp[-1] + 2 * dp[-2])
    
print(dp[n-1]%10_007)