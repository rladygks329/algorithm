import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    duration, earn = map(int, sys.stdin.readline().rstrip().split())
    finish_time = duration + i + 1
    arr.append((i+1, finish_time, earn))
arr.sort(key=lambda x:(x[1], -x[2]))

dp = [0 for i in range(n + 2)]

for i in range(1, n+2):
    for start, end, earn in arr:
        if i >= end and end <= n + 1:
            dp[i] = max(dp[i], dp[i-1], dp[start] + earn)
print(dp[-1])