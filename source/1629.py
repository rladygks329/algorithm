import sys

a, b, c = map(int, sys.stdin.readline().split())


def helper(x):
    if x == 1:
        return a%c
    if x%2 == 0:
        i = helper(x//2)
        return (i*i)%c
    else:
        i = helper(x//2)
        return (i*i*a)%c

print(helper(b))
