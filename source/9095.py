import sys

n = int(input())
for i in range(n):
    target = int(input())
            
    dp = [0 for i in range(target + 1)]
    
    if(target < 0):
        print(0)
        continue
    
    if(target > 0):
        dp[1] = 1
    if(target > 1):
        dp[2] = 2
    if(target > 2):
        dp[3] = 4
        
    for j in range(4, target+1):
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    print(dp[target])
         