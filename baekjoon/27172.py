import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

_max = max(arr)
_valid = [False] * (_max + 1)
answer = [0] * (_max + 1)

for i in arr:
    _valid[i] = True

for i in arr:
    for j in range(i + i, _max + 1, i):
        if _valid[j]:
            answer[j] -= 1
            answer[i] += 1

print(' '.join(map(str, [answer[i] for i in arr])))
