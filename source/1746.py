import sys

n, m = map(int, sys.stdin.readline().split())
stdin = sys.stdin.read().splitlines()

a = list(set(stdin[:n]) & set(stdin[n:]))
a.sort()

print(len(a))
for i in a:
    print(i)
