import sys
l, r, k = map(int, sys.stdin.read().splitlines())


def solve(start, limit, number):
    if start > limit:
        return 0

    result = limit//number
    result -= start // number
    if start % number == 0:
        result += 1

    if number == 2 and start <= 12:
        if result == 0:
            result = 0
        elif start == limit == 10:
            result = 1
        else:
            result -= 1
    return result

d = {
    2: 1,
    3: 3,
    4: 2,
    5: 5,
}
answer = solve(max(l, min), r, d[k])
print(answer)

'''
2 1 => 3이상인 1의 배수 3, 4, 5, 6, .....
3 3 => 6이상인 3의 배수, 6, 9, 12, ...
4 6 => 10이상인 2의 배수 (단 12가 아닌), 10, 14, 16, 18, 20, 22,....
5 10 => 15 이상인 5의 배수 15, 20, 25....
10  14 16 18 20
'''



