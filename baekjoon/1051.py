import sys

n, m = map(int, sys.stdin.readline().split())
arr = sys.stdin.read().splitlines()

limit = max(m, m)
ans = 0

for size in range(limit, -1, -1):
    for i in range(n-size):
        for j in range(m-size):
            if arr[i][j] == arr[i+size][j] == arr[i][j+size] == arr[i+size][j+size]:
                print((size+1)**2)
                sys.exit()

