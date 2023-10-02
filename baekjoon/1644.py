import sys
from math import sqrt

n = int(sys.stdin.readline())
MAX = 4_000_000
MAX = min(MAX, n)
arr = [1] * (MAX + 1)
s = []

if n < 3:
    print(n - 1)
    sys.exit()


def getPrimeNumber():
    arr[0] = arr[1] = 0
    for i in range(2, int(sqrt(MAX)) + 1):
        if not arr[i]:
            continue
        for j in range(i * 2, MAX + 1, i):
            arr[j] = 0

    for i in range(2, MAX + 1):
        if arr[i]:
            s.append(i)


getPrimeNumber()
start = end = 0
answer = 0
total = s[0]
while start <= end < len(s):
    if total < n:
        end += 1
        if end < len(s):
            total += s[end]
    else:
        total -= s[start]
        start += 1
    if total == n:
        answer += 1
print(answer)
