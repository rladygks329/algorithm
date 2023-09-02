import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

answer = -1000000
part_sum = -1

for num in arr:
    if part_sum <= 0:
        part_sum = 0
    part_sum += num
    answer = max(part_sum, answer)
print(answer)
