import sys
from collections import deque

n = int(sys.stdin.readline())
answer = [0] * (n+1)
graph = [[] for i in range(n+1)]

for _ in range(n-1):
    node1, node2 = map(int, sys.stdin.readline().rstrip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

q = deque()
q.append(1)

while q:
    cur = q.popleft()
    for node in graph[cur]:
        if answer[node] == 0:
            answer[node] = cur
            q.append(node)

for i in range(2, n+1):
    print(answer[i])

'''
1 6 
6 3 
3 5
4 1
2 4 
4 7
[0 1  2   3   4   5   6   7] => 해당 노드의 부모를 가르키는 배열
=> 높이를 비교해서 적은 곳으로 들어가기, 근데 같은 값이 들어오면 어떻게함?
1 6
'''