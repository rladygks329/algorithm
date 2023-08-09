#import sys
#sys.stdin = open("../input/1920.txt", "r")

n = input()
N = list(map(int, input().split()))
m = input()
M = list(map(int, input().split()))

N.sort()

# M이 N안에 존재하나
for m in M:
    exist = 0
    start = 0
    end = len(N)-1
    # == 하는 이유 1,4 -> 1,2 -> 2,2 로 진행될때 2,2가 실행안됨
    while (start <= end):
        mid = (start + end)//2
        if (m == N[mid]):
            exist = 1
            break
        elif (m < N[mid]):
            end = mid - 1
        else:
            start = mid+1
    print(exist)


