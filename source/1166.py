import sys

n, l, w, h = map(int, sys.stdin.readline().split())

start = 0
end = min(l, w, h)

for _ in range(100):
    mid = ( start + end ) / 2
    if (l // mid) * (w // mid) * (h//mid) >= n:
        start = mid
    else:
        end = mid

print("%.10f" %(end))
