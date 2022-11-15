_ = int(input())

for i in range(_):
    n = int(input())
    dp = [0 for j in range(101)]
    dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
    
    for j in range(6, n+1):
        dp[j] = dp[j-1] + dp[j-5]
    print(dp[n])