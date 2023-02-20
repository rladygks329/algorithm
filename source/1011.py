import sys

n = int(sys.stdin.readline())
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    length = end - start
    if length == 1:
        print(1)
        continue
    step = 1
    cur = 1
    while cur < length:
        mid = step//2
        if step%2:
            cur = (mid + 1) * (mid + 1)
        else:
            cur = mid * (mid + 1)
        #print(f'step:{step} 에서 갈 수 있는 최댓값은 {cur}입니다.')
        step += 1
    print(step-1)
