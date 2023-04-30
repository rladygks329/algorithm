import sys

n = int(sys.stdin.readline())
dice = list(map(int, sys.stdin.readline().split()))
a = dice[0]
b = dice[1]
c = dice[2]
d = dice[3]
e = dice[4]
f = dice[5]

dice2 = [a + b, a + c, a + d, a + e, b + c, b + d, b + f, c + e, c + f, d + e, d + f, e + f]
dice3 = [a+e+d, a+b+d, a+b+c, a+c+e, b+d+f, b+c+f, c+f+e, d+e+f, ]

def solve(n):
    if n == 1:
        return sum(dice) - max(dice)
    # 이웃한 3면의 합이 최소인거 4개
    # 이웃한 2면의 합이 최소인거  4 * (n-2) + 4 * (n-1) => 8n - 12
    # 1면의 값이 최소인거 (n-2)(n-2) * 5 + (n-2) * 4 = (5n-6)(n-2)
    a = min(dice3) * 4
    b = min(dice2) * (8*n - 12)
    c = min(dice) * (5*n-6) * (n-2)
    return a+b+c

print(solve(n))
