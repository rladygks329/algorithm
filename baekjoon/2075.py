import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

index = [n-1 for i in range(n)]
answer = 0
count = n
while count:
    tmp = [arr[index[i]][i] for i in range(n)]
    max_index = tmp.index(max(tmp))
    answer = tmp[max_index]
    index[max_index] -= 1
    count -= 1

print(answer)