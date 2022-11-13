from collections import deque


def D(n):
    return (n * 2) % 10000


def S(n):
    if(n == 0):
        return 9999
    return n-1


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


n = int(input())
for i in range(n):
    a, target = map(int, input().split())
    q = deque()
    visit = [False for i in range(10001)]
    ans = ["" for i in range(10001)]

    visit[a] = True
    q.append((a, ans[a]))

    while(not visit[target] and q):
        n, before = q.popleft()
        #print(f'n : {n}, before: {before}')
        arr = [(D(n), before + "D"), (S(n), before + "S"),
               (L(n), before + "L"), (R(n), before + "R")]
        #print(f'arr : {arr}')
        for i, j in arr:
            if(visit[i] == False):
                visit[i] = True
                ans[i] = j
                q.append((i, j))
    print(ans[target])
