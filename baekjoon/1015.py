import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
s_A = sorted(A)
P = [-1 for i in range(n)]

for i in range(n):
    P[i] = s_A.index(A[i])
    s_A[P[i]] = 0 #넣은 친구들은 0으로 만들어 중복처리

print(" ".join(map(str, P)))

