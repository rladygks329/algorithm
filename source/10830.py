import copy
import sys

n, b = map(int, sys.stdin.readline().split())
arr = []
s = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

answer = copy.deepcopy(arr)

def double():
    a = copy.deepcopy(answer)
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += a[i][k] * a[k][j]
            answer[i][j] = sum % 1000
def multiOne():
    a = copy.deepcopy(answer)
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += a[i][k] * arr[k][j]
            answer[i][j] = sum % 1000

def helper(n):
    if n <= 1:
        return
    if n%2 == 0:
        helper(n // 2)
        double()
    else:
        helper(n // 2)
        double()
        multiOne()

helper(b)
for i in range(n):
    for j in range(n):
        answer[i][j] = answer[i][j] % 1000

for i in answer:
    print(" ".join(map(str, i)))
