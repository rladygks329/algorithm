import sys
import re

n = int(sys.stdin.readline())
regex = re.compile("(100+1+|01)+")

for _ in range(n):
    stdin = sys.stdin.readline().rstrip()
    if re.fullmatch(regex, stdin):
        print("YES")
    else:
        print("NO")
