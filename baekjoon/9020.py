import sys

T = int(sys.stdin.readline())
problems = []

for _ in range(T):
    problems.append(int(sys.stdin.readline()))

MAX = max(problems)
arr = [True] * (MAX + 1)

for i in range(2, MAX + 1):
    if not arr[i]:
        continue
    for j in range(i+i, MAX + 1, i):
        arr[j] = False

for problem in problems:
    middle = problem // 2
    if arr[middle]:
        print(middle, middle)
        continue

    diff = 0
    while not arr[middle-diff] or not arr[middle+diff]:
        diff += 1

    print(middle-diff, middle + diff)

