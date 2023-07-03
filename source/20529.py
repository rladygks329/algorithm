import sys
from itertools import permutations

T = int(sys.stdin.readline())

for _ in range(T):
    nums = int(sys.stdin.readline())
    arr = sys.stdin.readline().split()
    s = set(arr)

    if len(arr) > 32:
        print(0)
    else:
        answer = 12
        for a, b, c in permutations(arr, 3):
            distance = 0
            for i in range(4):
                distance += (a[i] != b[i]) + (b[i] != c[i]) + (a[i] != c[i])
            answer = min(distance, answer)
        print(answer)
