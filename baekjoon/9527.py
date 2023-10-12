import sys

s, e = map(int, sys.stdin.readline().strip().split())
dp = [0] * 66

for i in range(1, 60):
    dp[i] = (i * 2**(i-1)) + 1
dp[0] = 1

def solve(n):
    n = list(str(bin(n).replace('0b', '')))

    size = len(n)
    result = 0
    count = 0

    for i in range(size):
        if n[i] == '1':
            result += dp[size - i - 1] + 2**(size - i - 1) * count
            count += 1
    return result

print(solve(e) - solve(s-1))
