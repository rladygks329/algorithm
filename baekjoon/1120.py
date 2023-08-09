import sys
s1, s2 = sys.stdin.readline().rstrip().split()
size1 = len(s1)
size2 = len(s2)
answer = 0

for i in range(size2 - size1 + 1):
    tmp = 0
    for j in range(size1):
        if s2[i + j] == s1[j]:
            tmp += 1
    answer = max(tmp, answer)

print(size1 - answer)