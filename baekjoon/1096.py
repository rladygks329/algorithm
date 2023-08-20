import sys

n = int(sys.stdin.readline())
print(bin(n).lstrip('0b').count('1'))
