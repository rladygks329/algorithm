import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
s = [0]

ans = 0
for i in data:
    ans += i
    s.append(ans)
    
for _ in range(m):
    i, j = map(lambda x: int(x)-1, sys.stdin.readline().split())
    print(s[j+1] - s[i])