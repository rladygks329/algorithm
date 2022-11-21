import sys

n = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()

ans = 0
cur = 0
for i in data:
    cur += i
    ans += cur

print(ans)
