import sys
import math
n = int(sys.stdin.readline())

def solve(n):
    if math.sqrt(n).is_integer():
        return 1

    s = {i**2 for i in range(1, int(math.sqrt(n)) + 1)}

    for a in s:
        if n - a in s:
            return 2

    for a in s:
        for b in s:
            if n - a - b in s:
                return 3
    return 4

print(solve(n))