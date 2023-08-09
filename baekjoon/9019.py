import sys
from collections import deque

def D(n):
    return (n * 2) % 10000


def S(n):
    return 9999 if n == 0 else n-1


def L(n):
    if(n < 1000):
        n *= 10
    else:
        tmp = n//1000
        n *= 10
        n %= 10000
        n += tmp
    return n


def R(n):
    tmp = n % 10
    n //= 10
    n += tmp * 1000
    return n


n = int(sys.stdin.readline())
for _ in range(n):
    start, target = map(int, sys.stdin.readline().split())
    visit = [False] * 10001
    visit[start] = 1
    q = deque()
    q.append([start, ""])

    while q:
        cur, ans = q.popleft()

        if cur == target:
            print(ans)
            break

        d = D(cur)
        if not visit[d]:
            visit[d] = True
            q.append([d, ans + "D"])

        s = S(cur)
        if not visit[s]:
            visit[s] = True
            q.append([s, ans + "S"])

        l = L(cur)
        if not visit[l]:
            visit[l] = True
            q.append([l, ans + "L"])

        r = R(cur)
        if not visit[r]:
            visit[r] = True
            q.append([r, ans + "R"])