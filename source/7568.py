import sys

n = int(sys.stdin.readline())
weight = []
height = []
answer = [0 for i in range(n)]

def compare(a, b):
    if(weight[a] > weight[b] and height[a] > height[b]):
        return 1
    elif(weight[a] < weight[b] and height[a] < height[b]):
        return -1
    else:
        return 0
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    weight.append(x)
    height.append(y)

# n^2으로 비교하기
for i in range(n-1):
    for j in range(i+1, n):
        if(compare(i,j) == 1):
            answer[i] += 1
        elif(compare(i,j) == 0):
            answer[i] += 1
            answer[j] += 1
        elif(compare(i,j) == -1):
            answer[j] += 1

for i in range(n):
    print(n - answer[i] , end=" ")
print()