import sys

n = int(sys.stdin.readline())
# dict = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680,14200,73712, 365596] 아래 코드로 얻은 값
# print(dict[n])

queens = []
answer = 0
def valid(x, y):
    for a, b in queens:
        if x == a or y == b or abs(x-a) == abs(y-b):
            return False
    return True

def backTracking(x, count):
    if count == 0:
        global answer
        answer += 1
        return
    # 현재 세로 => n - count - 1
    for y in range(n):
        if valid(x, y):
            queens.append((x, y))
            backTracking(x+1, count-1)
            queens.pop()
    return

for i in range(n):
    queens.append((0, i))
    backTracking(1, n-1)
    queens.pop()
print(answer)
