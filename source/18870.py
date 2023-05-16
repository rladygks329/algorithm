import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dict = {x: i for i, x in enumerate(sorted(set(data)))}
print(" ".join(map(str, [dict[i] for i in data])))