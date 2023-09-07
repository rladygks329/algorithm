import sys
from copy import deepcopy
from collections import deque
n = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().strip().split()))for i in range(n)]

def Up(m):
    arr = deepcopy(m)
    valid = [[True] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                continue
            index = i
            while index - 1 >= 0:
                #한칸 땡기기
                if arr[index-1][j] == 0:
                    arr[index-1][j], arr[index][j] = arr[index][j], 0
                    valid[index - 1][j], valid[index][j] = valid[index][j], True
                    index -= 1
                #같을 때
                elif arr[index-1][j] == arr[index][j]:
                    if not valid[index - 1][j]:
                        break
                    valid[index - 1][j] = False
                    arr[index - 1][j] *= 2
                    arr[index][j] = 0
                else:
                    break
    return arr
def Down(m):
    arr = deepcopy(m)
    valid = [[True] * n for i in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(n):
            if arr[i][j] == 0:
                continue
            index = i
            while index + 1 < n:
                # 한칸 땡기기
                if arr[index + 1][j] == 0:
                    arr[index + 1][j], arr[index][j] = arr[index][j], 0
                    valid[index + 1][j], valid[index][j] = valid[index][j], True
                    index += 1
                # 같을 때
                elif arr[index + 1][j] == arr[index][j]:
                    if not valid[index + 1][j]:
                        break
                    valid[index + 1][j] = False
                    arr[index + 1][j] *= 2
                    arr[index][j] = 0
                else:
                    break
    return arr

def Left(m):
    arr = deepcopy(m)
    valid = [[True] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                continue
            index = j
            while index - 1 >= 0:
                # 한칸 땡기기
                if arr[i][index - 1] == 0:
                    arr[i][index - 1], arr[i][index] = arr[i][index], 0
                    valid[i][index - 1], valid[i][index] = valid[i][index], True
                    index -= 1
                # 같을 때
                elif arr[i][index - 1] == arr[i][index]:
                    if not valid[i][index - 1]:
                        break
                    valid[i][index - 1] = False
                    arr[i][index - 1] *= 2
                    arr[i][index] = 0
                else:
                    break
    return arr
def Right(m):
    arr = deepcopy(m)
    valid = [[True] * n for i in range(n)]

    for i in range(n):
        for j in range(n-1, -1, -1):
            if arr[i][j] == 0:
                continue
            index = j
            while index + 1 < n:
                # 한칸 땡기기
                if arr[i][index + 1] == 0:
                    arr[i][index + 1], arr[i][index] = arr[i][index], 0
                    valid[i][index + 1], valid[i][index] = valid[i][index], True
                    index += 1
                # 같을 때
                elif arr[i][index + 1] == arr[i][index]:
                    if not valid[i][index + 1]:
                        break
                    valid[i][index + 1] = False
                    arr[i][index + 1] *= 2
                    arr[i][index] = 0
                else:
                    break
    return arr

answer = 0
q = deque()
q.append((0, graph))
while q:
    count, m = q.popleft()
    if count == 5:
        max_list = list(map(max, m))
        max_list.append(answer)
        answer = max(max_list)
        continue
    q.append((count + 1, Up(m)))
    q.append((count + 1, Down(m)))
    q.append((count + 1, Left(m)))
    q.append((count + 1, Right(m)))

print(answer)