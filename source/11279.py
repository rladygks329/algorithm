import sys
from heapq import heappop, heappush

_ = int(sys.stdin.readline())
arr = []

for _ in range(_):
    n = int(sys.stdin.readline())
    if(n > 0):
        heappush(arr, -n)
    else:
        if(arr):
            print(-arr[0])
            heappop(arr)
        else:
            print(0)
            
    