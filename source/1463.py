import sys

n = int(sys.stdin.readline())
# data[i] = 가는데 필요한 최소 수
data = [100000 for i in range(n+1)]
data[1] = 0
for i in range(2, n+1):
    if(i%2 == 0 and i%3 == 0):
        data[i] = min(data[i-1],data[i//2],data[i//3])
    elif(i%2 == 0):
        data[i] = min(data[i-1],data[i//2])
    elif(i%3 == 0):
        data[i] = min(data[i-1], data[i // 3])
    else:
        data[i] = data[i-1]
    data[i] += 1

print(data[n])



