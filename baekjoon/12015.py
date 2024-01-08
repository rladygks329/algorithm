import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = [arr[0]]

for i in range(1, n):
    if arr[i] > answer[-1]:
        answer.append(arr[i])
    else:
        index = bisect_left(answer, arr[i])
        answer[index] = arr[i]
print(len(answer))
