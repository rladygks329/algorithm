import sys

def solve(n, k):
    #누나가 더 멀리 있으면 뒤로는 1칸씩 가기 때문
    if(n >= k):
        return n-k

    dp = [0 for i in range(k + 2)]  # dp[k] = k까지 가는 최소값

    for i in range(n):
        dp[i] = n - i

    # n+1 to k+1 인이유 : dp[n] = 0이므로 수정할 필요 x, dp[k+1]-1 이 해가 될 수 있기 때문에 k+1까지 검증을 해야함
    for i in range(n + 1, k + 2):
        if (i % 2 == 0):
            #2로 나눠지면 2배를 가거나 1칸을 가거나 이동할 수 있고,
            # 이때 i-1의 dp 값을 갱신해줘야함, 더 큰 숫자로 이동하고 -1 하는게 더 빠를 수 있기 때문이다.
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
            dp[i-1] = min(dp[i] + 1, dp[i-1])
        else:
            dp[i] = dp[i - 1] + 1

    return dp[k]

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    print(solve(n, k))