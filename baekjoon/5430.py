import sys
from _collections import deque

arr = []


def solve(orders):
    q = deque(arr)
    sign = True

    for order in orders:
        if(order == "R"):
            sign = not sign
        elif(order == "D"):
            if(not q):
                print("error")
                return
            if(sign):
                q.popleft()
            else:
                q.pop()
    if(not sign):
        q.reverse()
    print(f'[{",".join(list(q))}]')


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    for _ in range(n):
        orders = sys.stdin.readline()
        orders.replace("RR", "")
        size = sys.stdin.readline()
        arr = filter(None, sys.stdin.readline().rstrip()[1:-1].split(","))
        solve(orders)
