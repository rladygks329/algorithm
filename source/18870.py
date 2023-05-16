import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
s = [(data[i], i) for i in range(n)] # value, index
s.sort()

prev = s[0][0]
cur = 0
for i in range(n):
    value, index = s[i]
    if prev != value:
        cur += 1
    data[index] = cur
    prev = value

for i in data:
    print(i, end=" ")
print()