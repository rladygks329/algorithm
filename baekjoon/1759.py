import sys

n, m = map(int, sys.stdin.readline().split())
arr = sys.stdin.readline().strip().split()
arr.sort()

tmp = []
answer = []

def backTracking():
    if len(tmp) == n:
        count = 0
        for c in tmp:
            if c in "aieou":
                count += 1
        if count >= 1 and n-count >= 2:
            answer.append("".join(tmp))
        return
    for i in range(m):
        if not tmp or (tmp and arr[i] > tmp[-1]):
            tmp.append(arr[i])
            backTracking()
            tmp.pop()
    return

backTracking()
print("\n".join(answer))