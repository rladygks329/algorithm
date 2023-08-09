import sys

n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    ans = 1
    for i in range(a):
        ans *= b
        b -= 1
    for i in range(1, a+1):
        ans //= i
    print(ans)