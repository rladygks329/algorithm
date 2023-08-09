import sys

n = int(sys.stdin.readline())

data = []
for i in range(n):
    num = int(sys.stdin.readline())
    if(num):
        data.append(num)
    else:
        data.pop()

print(sum(data))
