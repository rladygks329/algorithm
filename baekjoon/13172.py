import sys

T = int(sys.stdin.readline())
NUM = 1_000_000_007
answer = 0

def square(a, n):
    cur = 1
    add = 1
    s = {1 : a}
    while cur < n:
        if cur + add <= n:
            a = (a * s[add]) % NUM
            cur += add
            add *= 2
            s[cur] = a
        else:
            add //= 2
    return a%NUM
def solver(a, b):
    inverse_b = square(b, NUM - 2)
    return (a * inverse_b)%NUM

for _ in range(T):
    b, a = map(int, sys.stdin.readline().split())
    answer += solver(a, b)
print(answer%NUM)
