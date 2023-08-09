import sys

data = []

def solve(x, y, n):
    # 최소 리턴 조건
    if (n == 1):
        return data[x][y]

    #압축되는지 검사
    for i in range(n):
        for j in range(n):
            if (data[x + i][y + j] != data[x][y]):
                n //= 2
                # 압축 불가능 하니 4가지로 쪼개서 다시 실행
                return ("(" + solve(x, y, n)
                        + solve(x, y + n, n)
                        + solve(x + n, y, n)
                        + solve(x + n, y + n, n) + ")")

    # 압축 될 수 있으면 data[x][y]
    return data[x][y]


if __name__ == "__main__":
    # 변수 입력 부분
    n = int(sys.stdin.readline())
    data = sys.stdin.read().splitlines()

    # solve
    print(solve(0, 0, n))
