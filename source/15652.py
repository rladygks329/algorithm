import sys

n, m = map(int, sys.stdin.readline().split())
arr = [i+1 for i in range(n)]
answer = []
def backTracking(index, count):
    global n
    if count == 0:
        print(" ".join(map(str, answer)))
    else:
        for i in range(index, n):
            answer.append(arr[i])
            backTracking(i, count-1)
            answer.pop()

    return

backTracking(0, m)
