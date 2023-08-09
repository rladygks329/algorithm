import sys
import _collections

def BFS(start):
    distance = [0 for i in range(n + 1)]
    q = _collections.deque()
    q.append(start)
    checked[start] = 1
    while q:
        cur = q.popleft()
        for i in range(1, n+1):
            if(data[cur][i] and checked[i] == 0):
                checked[i] = 1
                q.append(i)
                distance[i] = distance[cur] + 1
    return sum(distance)

n, m = map(int, sys.stdin.readline().split())
data = [[0 for i in range(n+1)] for j in range(n+1)]
checked = [0 for i in range(n+1)]

for i in range(m):
    x,y = map(int, sys.stdin.readline().split())
    data[x][y] = 1
    data[y][x] = 1

min = 1001
ans = 1
for i in range(1, n+1):
    checked = [0 for i in range(n + 1)]
    cabin_num = BFS(i)
    if(cabin_num < min):
        min = cabin_num
        ans = i
print(ans)