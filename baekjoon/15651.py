import sys

n, m = map(int, sys.stdin.readline().strip().split())
answer = []

def solve():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):
        answer.append(i)
        solve()
        answer.pop()
solve()