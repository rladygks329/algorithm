import sys

n = int(sys.stdin.readline())
dict = {}

for _ in range(n):
    node, left, right = sys.stdin.readline().rstrip().split(" ")
    dict[node] = [left, right]

def preOrder(ch):
    if ch == ".":
        return ""
    return ch + preOrder(dict[ch][0]) + preOrder(dict[ch][1])

def inOrder(ch):
    if ch == ".":
        return ""
    return inOrder(dict[ch][0]) + ch + inOrder(dict[ch][1])

def nextOrder(ch):
    if ch == ".":
        return ""
    return nextOrder(dict[ch][0]) + nextOrder(dict[ch][1]) + ch


print(preOrder("A"))
print(inOrder("A"))
print(nextOrder("A"))