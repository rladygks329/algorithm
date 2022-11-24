import sys

n = int(sys.stdin.readline())

valid = [0 for i in range(21)]

for _ in range(n):
    orders = sys.stdin.readline().split()
    order = orders[0]
    if order == "add":
        valid[int(orders[1])] = 1
    elif order == "remove":
        valid[int(orders[1])] = 0
    elif order == "check":
        print(valid[int(orders[1])])
    elif order == "toggle":
        valid[int(orders[1])] ^= 1
    elif order == "all":
        valid = [1 for i in range(21)]
    elif order == "empty":
        valid = [0 for i in range(21)]
