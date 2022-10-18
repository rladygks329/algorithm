import sys
from _collections import deque

n = int(sys.stdin.readline())
order = sys.stdin.read().splitlines()

q = deque()
for i in order:
    if("push" in i):
        q.append(int(i.split()[1]))
    elif("pop" in i):
        print(q.popleft() if(q) else -1)
    elif("size" in i):
        print(len(q))
    elif("empty" in i):
        print(0 if(q) else 1)
    elif("front" in i):
        print(q[0] if(q) else -1)
    elif("back" in i):
        print(q[-1] if(q) else -1)