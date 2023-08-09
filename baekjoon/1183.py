import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append(a - b)

arr.sort()

if n%2 == 0:
    mid = n//2
    print(arr[mid] - arr[mid-1] + 1)
else:
    print(1)

