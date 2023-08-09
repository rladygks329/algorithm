import sys

target, n = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    cost, earn = map(int, sys.stdin.readline().split())
    arr.append((cost, earn))

dp = [[0 for i in range(target + 1)] for j in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, target + 1):
        cost, earn = arr[i-1]
        #계산한 값이랑 위의 항목에서의 값을 비교한다.
        tmp = []
        if dp[i-1][j] != 0:
            tmp.append(dp[i-1][j])
        if j - earn < 0:
            tmp.append(cost)
        else:
            tmp.append(dp[i][j - earn] + cost)
        dp[i][j] = min(tmp)


# for i in dp:
#     print(i)
print(dp[n][target])
''''''''''
돈, 사람 수, 몇개
    (사람 수)->     1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10 ,11, 12
cost, earn 물건     0  0  0  0  0  0  0  0  0  0   0   0
 3     5    0   0  3  3  3  3  3  6  6  6  6  6   9   9
 1     1    0   0  1  2  3  3  3  4  5  6  6  6   7   8 
'''