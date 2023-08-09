import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
count = int(sys.stdin.readline())

def solve(count):
    for i in range(n-1):
        max_value = arr[i]
        max_index = i
        for j in range(i+1, n):
            if j - i > count:
                break
            if arr[j] > max_value:
                max_value = arr[j]
                max_index = j
        for j in range(max_index, i, -1):
            arr[j] = arr[j-1]
        arr[i] = max_value
        count -= max_index - i

solve(count)
print( " ".join(map(str, arr)))

