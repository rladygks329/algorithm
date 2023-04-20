import sys

n, k = map(int, sys.stdin.readline().split())

count = 0
s = 0

while k:
    s = 1
    while 2 * s < n:
        s *= 2
    n -= s
    k -= 1

print(s-n if n > 0 else 0)
