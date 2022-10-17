import sys

_ = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
_ = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

dict = {}

for i in A:
    dict[i] = dict.get(i, 0) + 1

for i in B:
    print(dict.get(i,0), end=" ")
print()