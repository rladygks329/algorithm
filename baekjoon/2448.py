import sys

num = int(sys.stdin.readline())
answer = [[" " for i in range(2 * num)] for j in range(num)]
star = [[0, 0], [1, 1], [1, -1], [2, -2], [2, -1], [2, 0],[2, 1], [2, 2]]


def Recursion(n, x, y):
    if n == 3:
        for a, b in star:
            answer[x + a][y + b] = "*"
    else:
        middle = n//2
        Recursion(middle, x, y)
        Recursion(middle, x+middle, y+middle)
        Recursion(middle, x+middle, y-middle)

Recursion(num, 0, num-1)

for i in answer:
    print("".join(i))
print()
