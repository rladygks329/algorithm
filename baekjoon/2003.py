import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0
tmp = arr[0]
start = 0
end = 0

while end < n and start < n:
    # print(f'start : {start}, end : {end}, tmp: {tmp}')
    if tmp == m:
        answer += 1
        end += 1
        if end < n:
            tmp += arr[end]
    elif tmp < m:
        end += 1
        if end < n:
            tmp += arr[end]
    elif tmp > m:
        tmp -= arr[start]
        start += 1
print(answer)