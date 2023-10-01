import sys

n = int(sys.stdin.readline())
hanoi = [0, 0, 0]


def hanoi(num, start, end, other):
    if num > 0:
        hanoi(num - 1, start, other, end)
        print(start, end)
        hanoi(num - 1, other, end, start)


print(2**n - 1)
hanoi(n, 1, 3, 2)
