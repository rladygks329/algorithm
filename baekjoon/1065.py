import sys
def valid(n):
    if n < 10:
        return True

    s = str(n)
    arr = [int(i) for i in s]
    add = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if add != arr[i] - arr[i-1]:
            return False
    return True


n = int(sys.stdin.readline())

count = 0
for i in range(1, n + 1):
    if valid(i):
        count += 1
print(count)


