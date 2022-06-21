import sys
import math
#sys.stdin = open("../input/1929.txt", "r")

#입력받기
start, end = map(int, input().split())
#0 부터 검사하는 수 까지 bool 배열을 만든다 arr[i] = true -> i가 소수라는 뜻
arr = [True for i in range (0, end+1)]
#0과 1을 예외처리한다.
arr[0] = False
arr[1] = False
#소수를 검사하는 범위를 지정한다.  루트(최댓값) -> 올림
max = math.floor(math.sqrt(end+1))

#검사 aristoteles의 채
for i in range(2, max+1):
    x = i+i
    while(x < end+1):
        arr[x] = False
        x += i
#출력하는 부분
for i in range(start, len(arr)):
    if(arr[i]):
        print(i)