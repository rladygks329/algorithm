import sys

T = int(sys.stdin.readline())

for _ in range(T):
    arr = list(map(int, sys.stdin.readline().split()))[1:]

    major = 0
    count = 0

    for num in arr:
        if count == 0:
            major = num
            count = 1
        elif major == num:
            count += 1
        else:
            count -= 1

    length = len(arr)//2
    count = 0
    for num in arr:
        if num == major:
            count += 1

    print(major if count > length else "SYJKGW")