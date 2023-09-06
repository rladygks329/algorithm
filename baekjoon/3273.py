import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
target = int(sys.stdin.readline())

dict = {}
count = 0
for i in arr:
    if dict.get(i, 0) == 0:
        dict[target - i] = 1
    else:
        count += 1
print(count)