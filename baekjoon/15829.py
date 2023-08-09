import sys

n = int(sys.stdin.readline())
L = sys.stdin.readline().rstrip()

answer = 0
r = 1

for l in L:
    answer += ( ord(l) - 96 ) * r
    r *= 31
print(answer%1234567891)