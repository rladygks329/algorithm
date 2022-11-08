import sys, math

def solve(x, y, a, b):
    #a와 b는 항상 공약수의 배수만큼의 차가 난다. 즉 최대 공약수를 이용하여 판별할 수 있다. 
    gcd = math.gcd(x, y)
    if( (a-b) % gcd):
        return -1
    
    cur = b
    end = x*y
    while(cur <= end):
        if((cur-a)%x == 0):
            return cur
        cur += y 
        
    return -1

n = int(sys.stdin.readline())
for i in range(n):
    x, y, a, b = map(int, sys.stdin.readline().split())    
    print(solve(x, y, a, b))

'''
n년 - (x, y)  a, b
n -> n%x = a, n%y = b

즉 a,b 가 주어지면 
n -> a + x * 어떤 수 == b + y * 어떤 수
위 식에서 좌변의 어떤 수와 우변의 어떤 수는 다르다.

for문을 돌아가면서 한쪽을 기준으로 조사를 하면 된다.
n = (b + y * i)
n - a = x * 어떤 수
(n-a) % x = 0
'''