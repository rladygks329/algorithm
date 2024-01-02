import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.read().splitlines()))
d = {}

for num in arr:
    v = d.get(num, 0)
    d[num] = v + 1

for num in arr:
    sqrt = int(num ** 0.5)

    count = d[num] - 1
    if num != 1:
        count += d.get(1, 0)

    for i in range(2, sqrt + 1):
        if i*i == num:
            count += d.get(i, 0)
        elif num%i == 0:
            count += d.get(i, 0)
            count += d.get(num//i, 0)
    print(count, end=" ")
