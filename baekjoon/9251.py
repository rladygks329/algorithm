import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

n = len(A)
m = len(B)
arr = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
print(arr[n][m])

