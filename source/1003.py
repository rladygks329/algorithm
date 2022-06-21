#import sys
#sys.stdin = open("../input/1003.txt", "r")

def sol(x):
    if(x == 0):
        print(1, 0)
        return
    if(x == 1):
        print(0, 1)
        return
    x1, y1, x2, y2 = 1, 0, 0, 1
    while(1 < x):
        x1, y1, x2, y2 = x2, y2, x1+x2, y1+y2
        x -= 1
    print(x2, y2)

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
for i in data:
    sol(i)
