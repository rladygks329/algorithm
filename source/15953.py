import sys

def contestA(n):
    if n == 0 or n > 21:
        return 0
    if n > 15:
        return 100000
    if n > 10:
        return 300000
    if n > 6:
        return 500000
    if n > 3:
        return 2000000
    if n > 1:
        return 3000000
    return 5000000
def contestB(n):
    if n == 0 or n > 31:
        return 0
    if n > 15:
        return 320000
    if n > 7:
        return 640000
    if n > 3:
        return 1280000
    if n > 1:
        return 2560000
    return 5120000

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(contestA(a) + contestB(b))

