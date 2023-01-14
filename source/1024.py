import sys

def solve(n, l):
    ans = [-1]

    for i in range(l, 101):
        s = (i*(i-1))//2
        if n < s:
            break
        if (n - s)%i == 0:
            tmp = (n-s)//i
            ans = [tmp + j for j in range(i) ]
            break
    print(" ".join(map(str, ans)))


n, l = map(int, sys.stdin.readline().split())
solve(n, l)