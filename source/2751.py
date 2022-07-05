import  sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()

for i in data:
    print(i)