import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
INF = 100_000_000_000
answer = INF

_sum = 0
_count = 0
start = end = 0

while start <= end and start < len(arr):
    # print(f'start: {start} end: {end}, _sum : {_sum}, answer : {answer}, count : {_count}')
    if _sum < m:
        if end == len(arr):
            _sum -= arr[start]
            _count -= 1
            start += 1
            continue
        _sum += arr[end]
        _count += 1
        end += 1
    else:
        answer = min(answer, _count)
        _sum -= arr[start]
        _count -= 1
        start += 1
print(0 if answer == INF else answer)


