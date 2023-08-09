import sys

n = int(sys.stdin.readline())
data = []

## 입력을 받는 부분
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a,b))

## 회의가 빨리 끝나는 시간을 기준으로 정렬한다.
data.sort(key = lambda x : (x[1], x[0]))

##초기값은 첫번째 회의가 끝나는 시간, cur = 1 회의 1개는 있으니까
## iter를 돌면서 회의 시작시간이 끝나는 시간보다 같거나 크면 가능하다고 판단하고 cur , count를 갱신한다.
cur = data[0][1]
count = 1
for i in range(1, len(data)):
    if(data[i][0] >= cur):
        cur = data[i][1]
        count += 1
print(count)