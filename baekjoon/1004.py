import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    ans = 0
    for __ in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        a_in_circle = (x1-cx)**2 + (y1-cy)**2 <= r**2
        b_in_circle = (x2-cx)**2 + (y2-cy)**2 <= r**2
        if a_in_circle:
            ans += 1
        if b_in_circle:
            ans += 1
        if a_in_circle and b_in_circle:
            ans -= 2
    print(ans)
