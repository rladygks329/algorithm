import sys

def isRightTriangle(a, b, c):
    if(a > c):
        a, c = c, a
    if(b > c):
        b, c = c, b
    a = a * a
    b = b * b
    c = c * c
    print("right" if(c == a+b) else "wrong")


if __name__ == '__main__':
    while(True):
        a, b, c = map(int, sys.stdin.readline().split())
        if(a == 0 and b == 0 and c == 0):
            break;
        isRightTriangle(a, b, c)
