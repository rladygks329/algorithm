import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dpASC = [1] * n
dpDEC = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dpASC[i] = max(dpASC[i], dpASC[j] + 1)

for i in range(n-1, 0, -1):
    for j in range(i-1, -1, -1):
        if arr[j] > arr[i]:
            dpDEC[j] = max(dpDEC[j], dpDEC[i] + 1)

print(max([dpASC[i] + dpDEC[i] for i in range(n)]) - 1)
