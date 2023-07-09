import sys

def aToIdx(a):
    return ord(a) - 65

h, w = map(int, sys.stdin.readline().split())
arr = []

for i in range(h):
    arr.append(list(map(aToIdx, sys.stdin.readline().rstrip())))

alphabets = [False for i in range(26)]
alphabets[arr[0][0]] = True
answer = 0


def dfs(x, y, length):
    global answer
    if answer >= 26:
        return
    answer = max(length, answer)

    for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= a < h and 0 <= b < w and not alphabets[arr[a][b]]:
            alphabets[arr[a][b]] = True
            dfs(a, b, length + 1)
            alphabets[arr[a][b]] = False
    return


dfs(0, 0, 1)
print(answer)
