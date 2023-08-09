import sys
from collections import deque

stdin = sys.stdin.read().splitlines()
n = int(stdin[0])
arr = [list(map(int, i.split())) for i in stdin[1:]]
size = 2
count = 0
x, y = 0, 0
ans = 0

def findSP():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                arr[i][j] = 0
                return i, j
    return -1, -1
def BFS(a, b):
    q = deque([(a, b, 0)])
    visit = [[0 for i in range(n)] for j in range(n)]
    visit[a][b] = 1
    ans = []
    while q:
        px, py, dis = q.popleft()
        for dir_x, dir_y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            x1, y1 = px + dir_x, py + dir_y
            if x1 < 0 or x1 >= n:
                continue
            if y1 < 0 or y1 >= n:
                continue
            if visit[x1][y1] == 1:
                continue
            visit[x1][y1] = 1
            if arr[x1][y1] > size:
                continue
            if arr[x1][y1] == size or arr[x1][y1] == 0:
                q.append((x1, y1, dis + 1))
            else:
                ans.append((x1, y1, dis + 1))

    ans.sort(key=lambda point: (point[2], point[0], point[1]))
    if not ans:
        return -1, -1, -1
    return ans[0]

x, y = findSP()
while x != -1:
    x1, y1, dis = BFS(x, y)
    if x1 == -1:
        break
    ans += dis
    arr[x1][y1] = 0
    count += 1
    if count == size:
        size += 1
        count = 0
    x, y = x1, y1
print(ans)
