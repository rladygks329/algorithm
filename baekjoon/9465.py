import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    dp = [[0] * (n+1) for i in range(2)]

    arr = []
    arr.append(list(map(int, sys.stdin.readline().split())))
    arr.append(list(map(int, sys.stdin.readline().split())))



    if n == 1:
        print(max(arr[0][0], arr[1][0]))
        continue
    elif n == 2:
        print(max(arr[0][0] + arr[1][1], arr[0][1] + arr[1][0]))
        continue

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = dp[1][0] + arr[0][1]
    dp[1][1] = dp[0][0] + arr[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[0][i-2], dp[1][i-2]) + arr[0][i]
        dp[1][i] = max(dp[0][i-1], dp[1][i-2], dp[0][i-2]) + arr[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))
