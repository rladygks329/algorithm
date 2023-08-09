import sys
from _collections import deque

orders = sys.stdin.read().splitlines()
q = deque()

for order in orders:
    if("push_front" in order):
        q.appendleft(order.split()[1])
    elif("push_back" in order):
        q.append(order.split()[1])
    elif("pop_front" in order):
        print(q.popleft() if(q) else -1)
    elif ("pop_back" in order):
        print(q.pop() if (q) else -1)
    elif ("size" in order):
        print(len(q))
    elif ("empty" in order):
        print(0 if (q) else 1)
    elif ("front" in order):
        print(q[0] if (q) else -1)
    elif ("back" in order):
        print(q[-1] if (q) else -1)