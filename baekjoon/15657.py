import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

answer = []
tmp = []
def solver():
    if len(tmp) == m:
        answer.append(" ".join(map(str, tmp)))
        return
    for i in range(n):
        if tmp and arr[i] < tmp[-1]:
            continue
        tmp.append(arr[i])
        solver()
        tmp.pop()
    return

solver()
print("\n".join(answer))
