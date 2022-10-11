import sys
# 4 7
# 20 15 10 17

num, target = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

data.sort(reverse=True)

step = 1
index = 0
cur = 0
while(cur < target):
    cur += step
    data[index] -= 1
    if(data[index] == 0 or cur >= target):
        break
    if(data[index] <= data[index+1]):
        step += 1
        index += 1
print(data[index])