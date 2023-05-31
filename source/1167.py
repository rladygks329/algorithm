from sys import stdin

def bfs(start):
    max_length, end = 0, start
    visit = [0] * (n + 1)
    visit[start] = 1
    q = [(start, 0)]

    while q:
        cur, length = q.pop()
        if max_length < length:
            max_length = length
            end = cur

        for a, b in graph[cur]:
            if not visit[a]:
                q.append((a, length + b))
                visit[a] = 1

    return end, max_length


if __name__ == "__main__":
    n = int(stdin.readline())
    graph = [[] for i in range(n+1)]

    for i in range(1, n + 1):
        line = list(map(int, stdin.readline().split()))
        s = line[0]
        size = len(line)-1
        for j in range(1, size, 2):
            graph[s].append((line[j], line[j+1]))

    node, dis = bfs(1)
    node, dis = bfs(node)
    print(dis)

# 트리의 정점 구하는 문제
# 해당 요구사항은 트리라는 자료구조를 이해했을 때 더 쉽게 풀 수 있다.
# 트리의 가장 긴 거리인 지름의 경우에는 분명, 루트를 지나서 다른 노드로 가는 길일 것 이다.
# (루트를 안지날경우, 루트에서 나가는 길이 한개인 경우이다. 이 경우 최대길이는 루트에서 가장 깊은 노드까지)
# 그러므로, bfs를 통해 임의의 노드에서 반대편 트리에 있는 가장 깊은 노드로 이동할 수 있다.
# 마지막으로 해당 노드에서 다시 bfs를 하면 (반대편의 가장 깊은 노드) -> 루트 -> (이쪽에서 가장 깊은 노드)의 길을 찾을 수 있다.
