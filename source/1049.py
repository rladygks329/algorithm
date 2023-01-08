import sys

n, m = map(int, sys.stdin.readline().split())
ans = 0
six, one = 2000, 2000
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    six = min(six,i)
    one = min(one, j)
ans = min( (1 + (n//6))*six, n//6 * six + n%6 * one, n * one)
print(ans)