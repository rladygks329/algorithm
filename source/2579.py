import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    data.append(int(sys.stdin.readline()))

dp = [0 for i in range(n+1)]

if(n == 1):
    dp[1] = data[0]
elif(n == 2):
    dp[2] = data[0] + data[1]
elif(n == 3):
    dp[3] = max(data[0] + data[2], data[1]+data[2])
else:
    dp[1] = data[0]
    dp[2] = data[0] + data[1]
    dp[3] = max(data[0] + data[2], data[1]+data[2])
    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + data[i-1], dp[i-3] + data[i-2] + data[i-1])
print(dp[n])