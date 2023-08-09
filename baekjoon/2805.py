import sys

num, target = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

def calc(n):
    sum = 0
    for i in data:
        if(i>n):
            sum += i-n
    return sum

start = 0
end = max(data)
while(start <= end):
    mid = (start + end)//2
    if(calc(mid) < target):
        end = mid - 1
    else:
        start = mid + 1

print(end)

