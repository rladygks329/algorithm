import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

answer = []
s = set()
for i in combinations_with_replacement(arr, m):
    s.add(i)

print('\n'.join([' '.join(map(str, i)) for i in sorted(s)]))
