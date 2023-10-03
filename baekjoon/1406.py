import sys

T = int(sys.stdin.readline())
arr = []
answer = [1, 2, 4]

for _ in range(T):
    n = int(sys.stdin.readline())
    arr.append(n)


MAX = max(arr)
for i in range(4, MAX + 1):
    answer.append(sum(answer[-1:-4:-1])%1_000_000_009)

for i in arr:
    print(answer[i-1])
