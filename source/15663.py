import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

s = set()
for i in permutations(arr, m):
    s.add(i)

answer = list(s)
answer.sort()
for i in answer:
    print(" ".join(map(str, i)))