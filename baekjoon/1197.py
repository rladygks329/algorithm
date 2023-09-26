import sys
sys.setrecursionlimit(10001)

v, e = map(int, sys.stdin.readline().strip().split())
answer = 0
graph = []

for _ in range(e):
    start, end, w = map(int, sys.stdin.readline().strip().split())
    graph.append([w, start, end])
graph.sort()

root = [i for i in range(v + 1)]

def find(a):
    if root[a] == a:
        return a
    else:
        return find(root[a])


def union(a, b):
    p_a = find(a)
    p_b = find(b)
    if p_a < p_b:
        root[p_b] = root[p_a]
    else:
        root[p_a] = root[p_b]
    return


count = 0
index = 0
while count < v-1:
    w, start, end= graph[index]
    index += 1
    if find(start) == find(end):
        continue
    else:
        union(start, end)
        answer += w
        count += 1

print(answer)
