import sys

n = int(sys.stdin.readline())
answer = []
cur = []

def solve():
    for i in range(10):
        if not cur:
            cur.append(i)
            toInt()
            solve()
            cur.pop()
        elif cur and cur[-1] > i:
            cur.append(i)
            toInt()
            solve()
            cur.pop()
    return

def toInt():
    answer.append(int("".join(map(str, cur))))
    return

solve()
answer.sort()

if n >= len(answer):
    print(-1)
else:
    print(answer[n])

