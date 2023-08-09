import sys

n, target = map(int, sys.stdin.readline().split())
coins = []

for i in range(n):
    coins.append(int(input()))

coins.reverse()

count = 0
for coin in coins:
    if(target >= coin):
        tmp = target//coin
        target -= tmp * coin
        count += tmp
print(count)
