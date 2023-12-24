import sys
sys.setrecursionlimit(10 ** 6)
n, m, r = map(int, sys.stdin.readline().split())
visit = [False for i in range(n + 1)]
load = [[] for i in range(n + 1)]
answer = [0 for i in range(n + 1)]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    load[s].append(e)
    load[e].append(s)

for i in load:
    i.sort()

seq = 1

def DFS(R):
    global seq
    visit[R] = True
    answer[R] = seq
    seq += 1
    for x in load[R]:
        if not visit[x]:
            DFS(x)


DFS(r)
print('\n'.join(map(str, answer[1:])))