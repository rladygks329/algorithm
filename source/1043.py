import sys

n, m = map(int, sys.stdin.readline().split())
black_list = set(list(map(int, sys.stdin.readline().split()))[1:])
answer = 0
parties = []

def update(b):
    index = 0
    while index < m:
        a = parties[index]
        if a & b and a - b:
            b = b.union(a)
            index = 0
            continue
        index += 1
    return b


for _ in range(m):
    peoples = set(list(map(int, sys.stdin.readline().split()))[1:])
    parties.append(peoples)

black_list = update(black_list)
for party in parties:
    if not party & black_list:
        answer += 1
print(answer)
