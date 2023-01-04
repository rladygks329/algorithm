import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
s_A = sorted(A)
P = [-1 for i in range(n)]

for i in range(n):
    ans = 0 #A[i]가 몇번째로 큰지 찾아서
    for j in s_A:
        if A[i] > j:
            ans += 1
        else:
            break
    while ans in P:
        ans += 1
    P[i] = ans

print(" ".join(map(str, P)))
'''
3
2 3 1

B[P[0]] = A[0] = 2
B[P[1]] = A[1] = 3
B[P[2]] = A[2] = 1

P = [1 2 0] -> B[0]가 2번째로 큼, B[1]가 3번째로 큼, B[2]가 0번째로 큼

B[1] = 2
B[2] = 3
B[0] = 1

B = [1,2,3]

즉 n번의 원소가 몇번째인가
a.sort() = 123

'''
