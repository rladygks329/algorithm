import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(1, len(arr) + 1):
    for j in combinations(arr, i):
        if sum(j) == S:
            answer += 1

print(answer)