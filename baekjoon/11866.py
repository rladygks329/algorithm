import sys
from _collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque([i+1 for i in range(n)])
count = 1

print("<", end="")
while(q):
    if(count < k):
        count += 1
        q.append(q.popleft())
    elif(count == k):
        count = 1
        if(len(q) == 1):
            print(q.popleft(), end="")
        else:
            print(q.popleft(), end = ", ")
print(">")
