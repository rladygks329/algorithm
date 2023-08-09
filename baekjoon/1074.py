#import sys
#sys.stdin = open("../input/1074.txt", "r")

import sys
n, r, c = map(int, sys.stdin.readline().split())
cnt = 0

while(n > 0):
    mid = 2**(n-1) #중간값이지
    a,b = 0,0
    if(r < mid):
        a = 0
    else:
        a = 1
    if(c < mid):
        b = 0
    else:
        b = 1
    #print(r,c, mid)
    #print("중앙값은 : ", mid, "해당 점은 ", 2*a+b,"사분면에 있습니다", "더해지는 값은 ", (2*a+b) * mid * mid)
    cnt += (2*a+b) * mid * mid
    r -= a*mid
    c -= b*mid
    n -= 1
print(cnt)
