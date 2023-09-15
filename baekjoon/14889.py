import sys
from itertools import combinations
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().strip().split())) for i in range(n)]
answer = 20 * 20 * 100 + 1

row_sum = [sum(i) for i in arr]
col_sum = [sum(col) for col in zip(*arr)]
stat_per_member = [i+j for i, j in zip(row_sum, col_sum)]
total_sum = sum(row_sum)

for stat in combinations(stat_per_member, n//2):
    score = abs(total_sum - sum(stat))
    answer = min(score, answer)
print(answer)