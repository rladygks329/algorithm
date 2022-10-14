import sys

number = int(sys.stdin.readline())
for i in range(number):
    h, w, n = map(int, sys.stdin.readline().split())
    cur = 101
    height = 1
    weight = 2
    while(n  > 1):
        n -= 1
        if(height == h):
            height = 1
            cur = 100 + weight
            weight += 1
            continue
        cur += 100
        height += 1

    print(cur)


