import sys

answer = 0
n, score, p = map(int, sys.stdin.readline().split())

if n == 0:
    print(1)
    sys.exit()

arr = list(map(int, sys.stdin.readline().split()))
bigger = len(list(filter(lambda x: x > score, arr)))
same = arr.count(score)

print(bigger + 1 if bigger + same < p else -1)

