import sys

n = int(sys.stdin.readline().strip())
dp = [100] * (n + 1)
arr = []

for i in range(1, int(n ** 0.5) + 1):
    square = i * i
    dp[square] = 1
    arr.append(square)

for i in range(1, n + 1):
    for j in arr:
        if i - j > 0:
            dp[i] = min(dp[i], dp[i-j] + 1)
        else:
            break

print(dp[-1])
