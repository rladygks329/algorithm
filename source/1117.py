import sys

W, H, f, c, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

s_h = H//(c+1)
s_w = W - f

if f > W - f:
    s_w = f
    f = W - f

count = s_h * s_w - (x2 - x1) * (y2 - y1)
copy = 0

if f < x1:
    copy = f * s_h
elif x1 <= f <= x2:
    copy = f * s_h - (f-x1)*(y2-y1)
else:
    copy = f * s_h - (x2-x1)*(y2-y1)

print((count + copy) * (c + 1))
