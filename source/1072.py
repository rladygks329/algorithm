import sys
from decimal import *

x, y = map(int, sys.stdin.readline().split())
target = ((y*100)//x) + 1

if 100 <= target:
    print(-1)
    sys.exit()

s, e = 1, x
answer = 0
while s <= e:
    mid = (s+e)//2
    tmp = ((y+mid)*100)//(x+mid)

    if tmp < target:
        s = mid + 1
    else:
        answer = mid
        e = mid - 1
print(answer)


