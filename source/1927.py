import sys
from heapq import heappop, heappush

data = []
n = int(sys.stdin.readline())

for i in range(n):
    x = int(sys.stdin.readline())
    if(x == 0):
        print(heappop(data) if(data) else 0)
    else:
        heappush(data, x)
