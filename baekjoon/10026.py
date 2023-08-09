import sys

data = []


def DFS():
    n = len(data)
    visit = [[False for j in range(n)] for i in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if(visit[i][j]):
                continue
            s = [(i, j)]
            visit[i][j] = True
            letter = data[i][j]
            count += 1
            while(s):
                a, b = s.pop()
                for c, d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if(a + c < 0 or b + d < 0):
                        continue
                    if(a + c >= n or b + d >= n):
                        continue
                    if(visit[a+c][b+d] == False and data[a+c][b+d] == letter):
                        visit[a+c][b+d] = True
                        s.append((a+c, b+d))
    return count


if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        data.append(sys.stdin.readline().rstrip())
    print(DFS())

    for i in range(n):
        data[i] = data[i].replace("G", "R")
    print(DFS())
