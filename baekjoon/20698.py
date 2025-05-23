import sys

def find_optimal_L_W(stations):
    xs = sorted([x for x, y in stations])
    ys = sorted([y for x, y in stations])
    n = len(stations)

    cx = (xs[0] + xs[-1])//2
    cy = (ys[0] + ys[-1])//2

    L = max(abs(x - cx) for x, _ in stations)
    W = max(abs(y - cy) for _, y in stations)

    return L, W

n = int(sys.stdin.readline())
stations = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    stations.append((x, y))

L, W = find_optimal_L_W(stations)
print(L, W)