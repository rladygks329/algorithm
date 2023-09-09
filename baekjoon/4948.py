import sys
import math

element = int(sys.stdin.readline())
stdin = []

while element != 0:
    stdin.append(element)
    element = int(sys.stdin.readline())

max_v = 0
if stdin:
    max_v = 2 * max(stdin)
    dp = [True] * (max_v + 1)
else:
    dp = []

for i in range(2, int(math.sqrt(max_v))+1):
    for j in range(i + i, max_v+1, i):
        dp[j] = False

for i in stdin:
    count = 0
    for j in range(i+1, i + i + 1):
        if dp[j]:
            count += 1
    print(count)


