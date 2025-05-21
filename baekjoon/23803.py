import sys

n = int(sys.stdin.readline())
print("\n".join([ "@" * n if i < 4*n else "@" * n * 5 for i in range(5 * n)]))
