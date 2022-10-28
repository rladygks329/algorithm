import sys


global data

data = []
zero, one, minus = 0,0,0

def isValid(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if(data[x][y] != data[i][j]):
                return False
    return True

def solve(x, y, n):
    global zero
    global one
    global minus
    if(isValid(x, y , n) == False):
        n //= 3
        solve(x, y, n)
        solve(x, y+n, n)
        solve(x, y+2*n, n)

        solve(x+n, y, n)
        solve(x+n, y + n, n)
        solve(x+n, y + 2 * n, n)

        solve(x+2*n, y, n)
        solve(x+2*n, y + n, n)
        solve(x+2*n, y + 2 * n, n)
    else:
        if(data[x][y] == 0):
            zero += 1
        elif(data[x][y] == 1):
            one += 1
        else:
            minus += 1


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    stdin = sys.stdin.read().splitlines()


    for i in stdin:
        data.append(list(map(int, i.split())))

    solve(0, 0, n)

    print(minus)
    print(zero)
    print(one)

