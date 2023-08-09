import sys

n = int(sys.stdin.readline())

if(n < 3):
    print(n)
    sys.exit()

a, b = 1, 2
for i in range(n-2):
    a, b = b, a+b

print(b % 10007)