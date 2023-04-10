import sys

_ = int(sys.stdin.readline())

_map = {
    0: [10],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
}

for i in range(_):
    a, b = map(int, sys.stdin.readline().split())

    number_of_multiple = a%10
    index = b%len(_map[number_of_multiple]) - 1
    print(_map[number_of_multiple][index])
