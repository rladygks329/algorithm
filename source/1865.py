import sys

TC = int(sys.stdin.readline())

for _ in range(TC):
    n, m, w = map(int, sys.stdin.readline().split())
    graph = []

    for i in range(m):
        S, E, T = map(int, sys.stdin.readline().split())
        graph.append((S, E, T))
        graph.append((E, S, T))

    for i in range(w):
        S, E, T = map(int, sys.stdin.readline().split())
        graph.append((S, E, -T))

    answer = "NO"
    INF = 5000 * 10000
    distance = [INF for i in range(n + 1)]
    distance[1] = 0

    for i in range(1, n+1):
        for s, e, t in graph:
            if distance[e] > distance[s] + t:
                distance[e] = distance[s] + t
                if i == n:
                    answer = "YES"
    print(answer)
