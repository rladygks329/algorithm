import sys
from collections import defaultdict

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

dic = defaultdict(int)
answer = 0

for i in range(len(A)):
    sum = 0
    for j in range(i, len(A)):
        sum += A[j]
        dic[sum] = dic[sum] + 1

for i in range(len(B)):
    sum = 0
    for j in range(i, len(B)):
        sum += B[j]
        if dic[T-sum]:
            answer += dic[T-sum]
print(answer)
