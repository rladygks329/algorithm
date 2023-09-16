import sys
from itertools import permutations
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
answer = 0

for p in permutations(arr):
    s = 0
    for i in range(1, n):
        s += abs(p[i-1] - p[i])
    answer = max(s, answer)
print(answer)
