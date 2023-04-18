import sys


def solve(arr, target):

    if target in arr:
        return 0

    arr.sort()
    prev, next = 0, 0

    for d in arr:
        if d > target:
            next = d
            break
        prev = d

    return (target - prev) * (next - target) - 1


sys.stdin.readline()
data = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

ans = solve(data, target)
print(ans)
