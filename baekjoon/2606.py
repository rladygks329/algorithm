import sys

#입력 부분
n = int(sys.stdin.readline())
nodes = int(sys.stdin.readline())

data = [[0 for i in range(n)] for i in range(n)]
valid = [True for i in range(n)]

for i in range(nodes):
    a, b = map(lambda x: int(x)-1, sys.stdin.readline().split())
    data[a][b] = 1
    data[b][a] = 1

#초기값 설정
valid[0] = False
count = 0
stack = [0]

#깊이 우선 탐색
while(stack):
    i = stack.pop()
    for j in range(n):
        if (valid[j] and data[i][j] == 1):
            valid[j] = False
            count += 1
            stack.append(j)

#출력하는 부분 : 바이러스에 영향받은 컴퓨터의 수
print(count)
