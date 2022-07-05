import sys
n = int(sys.stdin.readline())
count = 0

for i in range(1, n+1):
    tmp = i
    while(tmp%5 == 0):
        count += 1
        tmp /= 5
print(count)