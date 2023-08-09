import sys

n = int(sys.stdin.readline())
min_arr = [0, 0, 0]
max_arr = [0, 0, 0]

for _ in range(n):
    input = list(map(int, sys.stdin.readline().split()))
    min_a1 = min(min_arr[0], min_arr[1]) + input[0]
    max_a1 = max(max_arr[0], max_arr[1]) + input[0]

    min_a2 = min(min_arr[0], min_arr[1], min_arr[2]) + input[1]
    max_a2 = max(max_arr[0], max_arr[1], max_arr[2]) + input[1]

    min_a3 = min(min_arr[1], min_arr[2]) + input[2]
    max_a3 = max(max_arr[1], max_arr[2]) + input[2]

    min_arr[0] = min_a1
    min_arr[1] = min_a2
    min_arr[2] = min_a3

    max_arr[0] = max_a1
    max_arr[1] = max_a2
    max_arr[2] = max_a3

print( max(max_arr), min(min_arr))