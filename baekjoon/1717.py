import sys
sys.setrecursionlimit(1_000_001)

n, m = map(int, sys.stdin.readline().strip().split())
arr = [i for i in range(n + 1)]

def union(x, y):
    p_x = getParent(x)
    p_y = getParent(y)

    if p_x < p_y:
        arr[p_y] = p_x
    else:
        arr[p_x] = p_y
    return

def getParent(x):
    if arr[x] == x:
        return arr[x]
    return getParent(arr[x])

for i in range(m):
    num, a, b = map(int, sys.stdin.readline().strip().split())
    if num == 1 and a == b:
        print('yes')
        continue

    if num == 0:
        if a != b:
            union(a, b)
    else:
        print('yes' if getParent(a) == getParent(b) else 'no')