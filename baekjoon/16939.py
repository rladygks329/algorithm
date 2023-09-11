import sys
from copy import deepcopy

arr = list(map(int, sys.stdin.readline().strip().split()))
answer = 0

def isValid(cube):
    for i in range(6):
        color = cube[i * 4]
        for j in range(4):
            if cube[i*4 + j] != color:
                return False
    return True
def calc(n, cube):
    # 0 ~ 3 세로로
    if n == 0: #left up
        cube[0], cube[2], cube[4], cube[6], cube[8], cube[10], cube[21], cube[23] = \
            cube[4], cube[6], cube[8], cube[10], cube[21], cube[23], cube[0], cube[2]
        # 붙어 있는 면 회전
        cube[12], cube[13], cube[14], cube[15] = cube[13], cube[15], cube[12], cube[14]
    elif n == 1: #left down
        cube[0], cube[2], cube[4], cube[6], cube[8], cube[10], cube[21], cube[23] = \
            cube[21], cube[23], cube[0], cube[2], cube[4], cube[6], cube[8], cube[10]
        cube[12], cube[13], cube[14], cube[15] = cube[14], cube[12], cube[15], cube[13]
    elif n == 2: #right up
        cube[1], cube[3], cube[5], cube[7], cube[9], cube[11], cube[20], cube[22] = \
            cube[5], cube[7], cube[9], cube[11], cube[20], cube[22], cube[1], cube[3]
        cube[16], cube[17], cube[18], cube[19] = cube[18], cube[16], cube[19], cube[17]
    elif n == 3: #right down
        cube[1], cube[3], cube[5], cube[7], cube[9], cube[11], cube[20], cube[22] = \
            cube[20], cube[22], cube[1], cube[3], cube[5], cube[7], cube[9], cube[11]
        cube[16], cube[17], cube[18], cube[19] = cube[17], cube[19], cube[16], cube[18]
    # 4 - 7 가로로
    elif n == 4: #up left
        cube[4], cube[5], cube[16], cube[17], cube[20], cube[21], cube[12], cube[13] = \
            cube[16], cube[17], cube[20], cube[21], cube[12], cube[13], cube[4], cube[5]
        cube[0], cube[1], cube[2], cube[3] = cube[2], cube[0], cube[3], cube[1]
    elif n == 5: #up right
        cube[4], cube[5], cube[16], cube[17], cube[20], cube[21], cube[12], cube[13] = \
            cube[12], cube[13], cube[4], cube[5], cube[16], cube[17], cube[20], cube[21]
        cube[0], cube[1], cube[2], cube[3] = cube[1], cube[3], cube[0], cube[2]
    elif n == 6: #down left
        cube[6], cube[7], cube[18], cube[19], cube[22], cube[23], cube[14], cube[15] = \
            cube[18], cube[19], cube[22], cube[23], cube[14], cube[15], cube[6], cube[7]
        cube[8], cube[9], cube[10], cube[11] = cube[9], cube[11], cube[8], cube[10]
    elif n == 7: #down right
        cube[6], cube[7], cube[18], cube[19], cube[22], cube[23], cube[14], cube[15] = \
            cube[14], cube[15], cube[6], cube[7], cube[18], cube[19], cube[22], cube[23]
        cube[8], cube[9], cube[10], cube[11] = cube[10], cube[8], cube[11], cube[9]
    elif n == 8: #top right
        cube[2], cube[3], cube[16], cube[18], cube[9], cube[8], cube[15], cube[13] = \
            cube[15], cube[13], cube[2], cube[3], cube[16], cube[18], cube[9], cube[8]
        cube[4], cube[5], cube[6], cube[7] = cube[6], cube[4], cube[7], cube[5]
    elif n == 9: #top left
        cube[2], cube[3], cube[16], cube[18], cube[9], cube[8], cube[15], cube[13] = \
            cube[16], cube[18], cube[9], cube[8], cube[15], cube[13], cube[2], cube[3]
        cube[4], cube[5], cube[6], cube[7] = cube[5], cube[7], cube[4], cube[6]
    elif n == 10: #bottom left
        cube[0], cube[1], cube[17], cube[19], cube[11], cube[10], cube[14], cube[12] = \
            cube[17], cube[19], cube[11], cube[10], cube[14], cube[12], cube[0], cube[1]
        cube[20], cube[21], cube[22],cube[23] = cube[22], cube[20], cube[23],cube[21]
    elif n == 11: #bottom right
        cube[0], cube[1], cube[17], cube[19], cube[11], cube[10], cube[14], cube[12] = \
            cube[14], cube[12], cube[0], cube[1], cube[17], cube[19], cube[11], cube[10]
        cube[20], cube[21], cube[22], cube[23] = cube[21], cube[23], cube[20], cube[22]

for i in range(12):
    cube = deepcopy(arr)
    calc(i, cube)
    if isValid(cube):
        answer = 1
        break
print(answer)

