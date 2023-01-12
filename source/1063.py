import sys
king, stone, n = sys.stdin.readline().split()
n = int(n)
king = (ord(king[0]), int(king[1]))
stone = (ord(stone[0]), int(stone[1]))
# 64 < x < 73

for _ in range(n):
    orders = sys.stdin.readline()
    x = 0
    y = 0
    for order in orders:
        if order == "R":
            x += 1
        elif order == "L":
            x -= 1
        elif order == "B":
            y -= 1
        elif order == "T":
            y += 1
    if stone[0] == king[0] + x and stone[1] == king[1] + y:
        if 64 < stone[0]+x < 73 and 0 < stone[1]+y < 9:
            king = (stone[0], stone[1])
            stone = (stone[0] + x, stone[1] + y)
        else:
            continue
    else:
        if 64 < king[0] + x < 73 and 0 < king[1] + y < 9:
            king = (king[0]+x, king[1]+y)

king = chr(king[0]) + str(king[1])
stone = chr(stone[0]) + str(stone[1])
print(f'{king}\n{stone}')

