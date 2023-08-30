import sys

MAN = 1
WOMAN = 2

n = int(sys.stdin.readline())
arr = list(map(lambda x: int(x) == 1, sys.stdin.readline().split()))
T = int(sys.stdin.readline())

for _ in range(T):
    gender, num = map(int, sys.stdin.readline().split())
    cur = num - 1

    arr[cur] = not arr[cur]

    if gender == MAN:
        cur += num
        while cur < n:
            arr[cur] = not arr[cur]
            cur += num
    else:
        left = cur - 1
        right = cur + 1
        while left >= 0 and right < n and arr[left] == arr[right]:
            arr[left] = not arr[left]
            arr[right] = not arr[right]
            left -= 1
            right += 1

index = 0
while index < len(arr):
    print("1" if arr[index] else "0", end=" ")
    if (index+1)%20 == 0:
        print()
    index += 1