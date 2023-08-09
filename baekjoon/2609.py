import sys

def gcd(x,y):
    if(x%y == 0):
        return y
    else:
        return gcd(y, x%y)
a,b = map(int, sys.stdin.readline().split())
if(b > a):
    a, b = b, a
c = gcd(a,b)
print(c)
print(int(a*b/c))