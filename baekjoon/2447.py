import sys

n = int(sys.stdin.readline())
answer = [['*' for i in range(n)] for j in range(n)]

def mkHole(x, y, n):
    if n <= 1:
        return
    n //= 3

    for i in range(n):
        for j in range(n):
            answer[x + n + i][y + n + j] = " "

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            mkHole(x + i * n, y + j * n, n)

mkHole(0, 0, n)
for i in answer:
    print("".join(i))

