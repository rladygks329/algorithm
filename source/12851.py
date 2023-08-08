import sys
from collections import deque
n, k = map(int, sys.stdin.readline().rstrip().split())
LIMIT = 100000 * 2 + 1
dp = [100000 + 1] * LIMIT #dp[n] = 누나가 n번을 가는데 필요한 최소 time
count = 0 #dp[n]을 최소로 갈 수 잇는 거리의 개수


q = deque()
q.append((n, 0))

while q:
    cur, depth = q.popleft()
    #print(f'cur = {cur}, depth = {depth}')
    if depth > dp[cur] or cur < 0 or cur > 100000:
        continue
    # end 조건
    if cur == k:
        if dp[cur] > depth:
            dp[cur] = depth
            count = 1
        elif dp[cur] == depth:
            count += 1
        continue
    else:
        dp[cur] = depth
        if cur > k:
            q.append((cur - 1, depth + 1))
        else:
            q.append((cur - 1, depth + 1))
            q.append((cur + 1, depth + 1))
            q.append((cur * 2, depth + 1))

print(dp[k])
print(count)
'''
시간과 방법의 가지 수
1. 200000 + 1 개의 배열을 만든다
2. 누나의 위치에서 DFS를 한다
3. queue에 (depth, cur)을 동시에 저장하며, 만약 depth가 더 낮으면 해당 dp를 초기화
아닐 경우는 +1을 한다.
4. end 조건은 cur 노드가 정상 범위를 벗어낫을 때 또는 멀리 돌아갔을 경우
'''
