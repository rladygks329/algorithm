import sys

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
data = []

def sol(x, y, n):
    #초기값 설정
    count = 1
    stack = [(x,y)]
    data[x][y] = 0

    #깊이 우선 탐색
    while(stack):
        a, b = stack.pop()
        for c,d in dir:
            if(a+c < 0 or b+d < 0):
                continue
            if(a+c >=n or b+d >= n):
                continue
            if(data[a+c][b+d] == 1):
                data[a+c][b+d] = 0
                stack.append((a+c,b+d))
                count+=1
    return count




if __name__ == "__main__":
    #입력을 받는 부분
    n = int(sys.stdin.readline())
    stdin = sys.stdin.read().splitlines()
    answer = []

    # string[] -> int[][]
    data = [[int(j) for j in i] for i in stdin]

    # 주택을 발견하면 인접 단지 수 찾기
    for i in range(n):
        for j in range(n):
            if(data[i][j]):
                answer.append(sol(i,j,n))
    #출력 부분
    answer.sort()
    print(len(answer))
    for i in answer:
        print(i)
