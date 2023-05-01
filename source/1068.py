import sys

n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
deleteNode = int(sys.stdin.readline())

def getRoot(n):
    while n >= 0:
        n = tree[n]
    return n

tree[deleteNode] = -2
count = 0
for i in range(n):
    root = getRoot(i)
    if root == -1 and tree.count(i) == 0:
        count += 1

print(count)
