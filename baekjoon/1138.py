import sys

n = int(sys.stdin.readline())
bigger = list(map(int, sys.stdin.readline().split()))

answer = [0 for i in range(n)]

for i in range(n):
    count = bigger[i] + 1

    for j in range(n):
        if not answer[j]:
            count -= 1
        if not count:
            answer[j] = i + 1
            break

print(" ".join(map(str, answer)))
