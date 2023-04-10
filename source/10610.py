import sys

number = list(sys.stdin.readline().rstrip())

if sum(map(int, number))%3 != 0:
    print(-1)
    sys.exit()

number.sort(reverse=True)

if number[-1] == "0":
    print( "".join(number))
else:
    print(-1)
