import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

#i번 노드를 탐색
for i in range(n):
    s = []
    for j in range(n):
        if(data[i][j] == 1):
            s.append(j)
    while(s):
        t = s.pop()
        for _ in range(n):
            if(data[t][_] == 1 and data[i][_] == 0):
                s.append(_)
                data[i][_] = 1
for i in data:
    print(" ".join(map(str, i)))