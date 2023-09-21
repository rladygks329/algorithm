import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

nextState = [
    [0, 2],
    [1, 2],
    [0, 1, 2]
]
nextCenter = [
    [0, 1],
    [1, 0],
    [1, 1]
]

def isValid(x, y, state):
    arr = [
        [[0, 0], [0, 1]],
        [[0, 0], [1, 0]],
        [[0, 0], [1, 0], [0, 1], [1, 1]]
    ]
    result = True
    for a, b in arr[state]:
        if x + a < n and y + b < n:
            if graph[x+a][y+b] != 0:
                result = False
                break
        else:
            result = False
            break
    return result
def isArrive(x, y, state):
    if state == 0:
        if x == n - 1 and y == n - 2:
            return True
    elif state == 1:
        if x == n - 2 and y == n - 1:
            return True
    elif state == 2:
        if x == n - 2 and y == n - 2:
            return True
    return False


answer = 0

if graph[n-1][n-1] != 0:
    print(0)
    sys.exit()

q = [(0, 0, 0)]
while q:
    x, y, state = q.pop()
    if isArrive(x, y, state):
        answer += 1
        continue
    nxt_x, nxt_y = x + nextCenter[state][0], y + nextCenter[state][1]
    for nxt_state in nextState[state]:
        if isValid(nxt_x, nxt_y, nxt_state):
            q.append((nxt_x, nxt_y, nxt_state))
print(answer)