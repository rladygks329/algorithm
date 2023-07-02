import sys

T = int(sys.stdin.readline())

for _ in range(T):
    arr = list(map(int, sys.stdin.readline().split()))[1:]
    s = {}

    length = len(arr)//2
    hasWinner = False
    answer = 0

    for num in arr:
        if num in s:
            s[num] += 1
        else:
            s[num] = 1

    for num, count in s.items():
        if count > length:
            hasWinner = True
            answer = num

    print(answer if hasWinner else "SYJKGW")