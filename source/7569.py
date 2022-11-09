import sys
from collections import deque
    
m, n, h = map(int, sys.stdin.readline().split())
data = [[list(map(int, sys.stdin.readline().split())) for j in range(n)] for i in range(h)]

dir = [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            # 방문하면서 찾아야할 것 : 토마토 시작 위치
            if(data[i][j][k] == 1):
                q.append((i, j, k))

#BFS      
while(q):
    i, j, k = q.popleft()
    for a, b, c in dir:
        _x, _y, _z = i+a, j+b, k+c 
        if(_x < 0 or _y < 0 or _z < 0):
            continue
        if(_x >= h or _y >= n or _z >= m):
            continue
        if(data[_x][_y][_z] == 0):
            # 1->2 -> 3 ,,,,,,n+1 까지 값이 변함
            # n은 몇번의 step이 반복했는지를 뜻함
            data[_x][_y][_z] = data[i][j][k] + 1
            q.append((_x, _y, _z))

#안익은 토마토가 있다면 두가지 경우가 있다.
#안익은 토마토만 처음부터 들어온 경우
#bfs가 돌았지만 고립되어 있는 경우 
# 두 가지 case 모두 -1을 리턴한다.
step = 0
for i in data:
    for j in i:
        for k in j:
            step = max(step, k)
            if(k == 0):
                print(-1)
                sys.exit()
print(step - 1)