import sys
from _collections import deque

#주어진 인자를 받는 부분
stdin = sys.stdin.read().splitlines()
x, y = map(lambda str: int(str)-1, stdin[0].split())

data = []
for i in stdin[1:]:
    tmp = []
    for j in i:
        tmp.append(int(j))
    data.append(tmp)

#문제를 푸는데 필요한 변수를 선언하는 부분
dir = [(0,1) , (1,0), (-1, 0), (0, -1)]
q = deque()
ans = []

#초기값
count = 1
data[0][0] = 0
q.append((0, 0, 0))


#BFS로 문제를 푸는 과정
while(q):
    a, b, count = q.popleft()
    count += 1
    if (a == x and b == y):
        ans.append(count)
        continue
    for w, h in dir:
        #q에 넣기전에 검사를 해준다.
        _x, _y = a + w,  b + h
        if (_x < 0 or _y < 0 or _x > x or _y > y):
            continue
        if (data[_x][_y] == 0):
            continue
        data[_x][_y] = 0
        q.append([_x, _y, count])
print(min(ans))