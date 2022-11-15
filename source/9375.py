import sys

n  = int(input())

for _ in range(n):
    __ = int(input())
    map = {}
    for j in range(__):
        line = input().split()
        if(line[1] not in map.keys()):
            map[line[1]] = 1
        else:
            map[line[1]] = map[line[1]] + 1
    result = 1
    for key in map.keys():
        result *= map[key] + 1
    print(result - 1)