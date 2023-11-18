import sys

n = int(sys.stdin.readline())
words = list(sys.stdin.read().splitlines())
valid = [True] * n
answer = 0


def is_like(a, b):
    if len(a) != len(b):
        return False

    dict = {}
    s = set()
    for i in range(len(a)):
        if a[i] not in dict:
            if b[i] in s:
                return False
            dict[a[i]] = b[i]
            s.add(b[i])
        else:
            if dict[a[i]] != b[i]:
                return False
    return True


for i in range(n - 1):
    if not valid[i]:
        continue
    count = 1
    for j in range(i + 1, n):
        if is_like(words[i], words[j]):
            valid[j] = False
            count += 1
    answer += count * (count - 1)//2

print(answer)


