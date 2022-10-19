import sys

answer = [0 for i in range(10001)]
n = int(sys.stdin.readline())

for i in range(n):
    a = int(sys.stdin.readline())
    answer[a] += 1
for i in range(1, 10001):
    for j in range(answer[i]):
        sys.stdout.write(str(i)+"\n")
