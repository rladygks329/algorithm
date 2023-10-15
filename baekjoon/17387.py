import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def CCW(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)


answer = 0
x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().strip().split())

p1 = Point(x1, y1)
p2 = Point(x2, y2)
p3 = Point(x3, y3)
p4 = Point(x4, y4)


if CCW(p1, p2, p3) * CCW(p1, p2, p4) <= 0 and CCW(p3, p4, p1) * CCW(p3, p4, p2) <= 0:
    if CCW(p1, p2, p3) * CCW(p1, p2, p4) == 0 and CCW(p3, p4, p1) * CCW(p3, p4, p2) == 0:
        if min(p1.x, p2.x) <= max(p3.x, p4.x) and min(p3.x, p4.x) <= max(p1.x, p2.x) and min(p1.y, p2.y) <= max(p3.y, p4.y) and min(p3.y, p4.y) <= max(p1.y, p2.y):
            answer = 1
    else:
        answer = 1

print(answer)










