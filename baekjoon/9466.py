import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    answer = 0
    arr = [0] + list(map(int, sys.stdin.readline().strip().split()))
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if visited[i]:
            continue
        if i == arr[i]:
            visited[i] = True
            answer += 1
            continue

        slow = fast = i
        while not visited[arr[slow]]:
            visited[arr[slow]] = True
            slow = arr[slow]
            fast = arr[arr[fast]]
            if fast == slow:
                answer += 1
                cycle = arr[slow]
                while cycle != slow:
                    visited[cycle] = True
                    cycle = arr[cycle]
                    answer += 1
                break
        visited[i] = True
    print(n - answer)