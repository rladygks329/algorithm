import sys

num, target = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
blackJack = 0

for i in range(0, num-2):
    for j in range(i+1, num-1):
        for k in range(j+1, num):
            cur = data[i] + data[j] + data[k]
            if(cur <= target and cur > blackJack):
                blackJack = cur
print(blackJack)