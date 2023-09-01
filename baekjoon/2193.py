import sys

n = int(sys.stdin.readline().rstrip())
dp = [0 for i in range(90 + 1)]
answer = 0

dp[1] = 1
dp[2] = 1
dp[3] = 2
for i in range(4, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])
'''
1 -> 1
2 -> 10
3 -> 101 100 
4 -> 1010, 1000, 1001,
5 -> 10000, 10100 10101 10001 10010
이전거 뒤에 0 붙이기
이전 이전거 뒤에 01 붙이기 

1 
10 
100     101
1000    1010    1001
10000   10100   10010   10001   10101
'''