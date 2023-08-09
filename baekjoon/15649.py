import sys
n, m = map(int, sys.stdin.readline().split())
answer = []
arr = [i for i in range(1, n+1)]
valid = [True for i in range(n)]


def backTracking(count):
    if count == 0:
        print(" ".join(map(str, answer)))
        return
    for i in range(n):
        if valid[i]:
            valid[i] = False
            answer.append(arr[i])
            backTracking(count-1)
            answer.pop()
            valid[i] = True
    return


backTracking(m)

