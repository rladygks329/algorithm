#import sys
#sys.stdin = open("../input/1107.txt", "r")

import sys
possible = [i for i in range(10)]

def valid(x):
    for i in str(x):
        if(possible[int(i)] == -1):
            return False
    return True

target = int(sys.stdin.readline())
broken = int(sys.stdin.readline())
data = []

if(broken):
    data = list(map(int, sys.stdin.readline().split()))
for i in data:
    possible[i] = -1

min = abs(target - 100)

for i in range(0, 2*target+10):
    if(valid(i)):
        tmp = abs(target-i) + len(str(i))
        if(tmp<min):
            min = tmp
print(min)
