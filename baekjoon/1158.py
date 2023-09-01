import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [i for i in range(1, n+1)]
index = m-1
answer = []

for i in range(n):
    answer.append(arr.pop(index))
    index += m-1
    if arr:
        index %= len(arr)
print("<"+", ".join(map(str, answer)) +">")