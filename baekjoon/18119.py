import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

def getTrimmedMean():
    if not arr:
        return 0

    size = len(arr)
    trim = round(size * 0.15)
    sub_arr = arr[trim:size - trim]
    return round(sum(sub_arr)/(len(sub_arr)))

def round(n):
    return int(n) + 1 if abs(int(n) - n) >= 0.5 else int(n)
print(getTrimmedMean())
