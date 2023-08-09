import sys

def calc(x):
    tmp = x
    count = 0
    while(tmp>0):
        count += tmp%10
        tmp //= 10
    return x+count

N = sys.stdin.readline()
n = int(N)
start = n - len(N)*9

exist = False
for i in range(start, n):
    if(calc(i) == n):
        print(i)
        exist = True
        break
if(not exist):
    print(0)