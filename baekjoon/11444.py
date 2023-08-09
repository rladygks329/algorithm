import sys

n = int(sys.stdin.readline())
dict = {1:1,2:1,3:2,4:3,5:5}
dividor = 1_000_000_007

def helper(n):
    if dict.get(n):
        return dict[n]

    mid = n // 2
    x = helper(mid)
    y = helper(mid-1)
    z = x + y

    if n%2 == 0:
        dict[n] = (z*x + x*y)%dividor
    else:
        dict[n] =(z*z + x*x)%dividor
    return dict[n]
print(helper(n))
# print(dict)
'''
f(n)  = f(n-1) f(n-2)
=> f(n-1) + f(n-2) = (1 1) k ==1 => (f(2) f(1)
=> 2 * f(n-2) + f(n-3)  (2, 1) k ==2 => (f(3) f(2)
=> 3 * f(n-3) + 2 * f(n-4) (3, 2)
=> 5f(n-4) + 3f(n-5)

 f(n) =  f(k+1)f(n-k) + f(k)f(n-k-1)

k+1, n-k, k, n-k-1 이 동일해지는 k의 값은?
k+1, k => n-k, n-k-1
 
 k+1 == n-k
 2k == n-1
 k = (n-1)//2
 
 if n == 5 
    k = 2

f(5) => f(3)f(3) + f(2)f(2)
f(n) = f(mid+1)f(mid+1) + f(mid)f(mid)
     => (f(mid-1)+f(mid))(f(mid-1)+f(mid)) + f(mid)f(mid)

if n == 6:
    k = 3
f(6) = f(4)f(3) + f(3)f(2)
     =>(f(2)+f(3))f(3) + f(3)f(2)

f(n) = (f(mid-1)+f(mid))f(mid) + f(mid)f(mid-1)
'''
