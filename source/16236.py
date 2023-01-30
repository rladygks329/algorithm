import sys
from collections import deque

stdin = sys.stdin.read().splitlines()
n = int(stdin[0])
arr = [list(map(int, i.split())) for i in stdin[1:]]
valid = [[0 for i in range(n)] for j in range(n)]
size = 2
count = 0
x, y = 0, 0
ans = 0

def findSP():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                return i, j
    return -1

x, y = findSP()
arr[x][y] = 0
valid[x][y] = 1
q = deque([(x, y)])


while q:
    px, py = q.popleft()
    for dir_x, dir_y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        x1, y1 = px + dir_x, py + dir_y
        if x1 < 0 or x1 >= n:
            continue
        if y1 < 0 or y1 >= n:
            continue
        if valid[x1][y1] == 1:
            continue
        if arr[x1][y1] > size:
            continue
        if arr[x1][y1] == size or arr[x1][y1] == 0:
            valid[x1][y1] = 1
            q.append((x1, y1))
        else:
            ans += abs(x - x1) + abs(y - y1)
            count += 1
            if count == size:
                size += 1
                count = 0
            arr[x1][y1] = 0
            x = x1
            y = y1
            q.clear()
            q.append((x1, y1))
            valid = [[0 for i in range(n)] for j in range(n)]
            print("########")
            for i in range(n):
                for j in range(n):
                    if i == x1 and j == y1:
                        print("X", end=" ")
                        continue
                    print(arr[i][j], end=" ")
                print(f'ans: {ans}')
            break
print(ans)