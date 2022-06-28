import sys
import _collections
#전역변수
data = []
checked = []
# 함수 선언
def DFS(target, n):
    #방문안햇으면
    if(checked[target]):
        return

    print(target, end=" ")
    checked[target] = 1

    for i in range(1, n+1):
        if(data[target][i]):
            DFS(i, n)
def BFS(target, n):
    q = _collections.deque()
    q.append(target)
    while q:
        num = q.popleft()
        if(checked[num] == 0):
            print(num, end=" ")
            checked[num] = 1
            for i in range(1, n+1):
                if (data[num][i] and checked[i] == 0):
                    q.append(i)
    return

#인풋 받는 부분
N, M, V = map(int, sys.stdin.readline().split())
data = [[0 for i in range(N+1)] for j in range(N+1)] # 더크게 만듬 data[n][m] -> n에서 m으로 갈수 있나
checked = [0 for k in range(N+1)]

for i in range(M):
    w,h = map(int, sys.stdin.readline().split())
    data[w][h] = 1
    data[h][w] = 1

DFS(V, N)
#방문 노드 초기화, 개행문자
checked = [0 for k in range(N+1)]
print()
BFS(V, N)


