import sys

answer = [0, 0]  # white / blue
data = []

#입력 받는 부분
n = int(sys.stdin.readline())
stdin = sys.stdin.read().splitlines()

#str -> int 배열 정리하기
for i in stdin:
    data.append(list(map(int, i.split())))

#중복된 if문을 제거하기위한 코드
def increaseAnwer(c):
    if(c):
        answer[1] += 1
    else:
        answer[0] += 1

#재귀로 풀기
def solve(x, y, n):
    if(n == 1):
        increaseAnwer(data[x][y])
        return
    for i in range(n):
        for j in range(n):
            if(data[x][y] != data[x+i][y+j]):
                n //= 2
                solve(x, y, n)
                solve(x+n, y, n)
                solve(x, y+n, n)
                solve(x+n, y+n, n)
                return
    increaseAnwer(data[x][y])
    return

solve(0, 0, n)
print(answer[0])
print(answer[1])
