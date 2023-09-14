import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))


index = 1
count = 0
find = False

while not find:
    d = set()
    s = ""
    tmp = True
    for file in arr:
        if index > len(file):
            s = "".join(map(str, file))
        else:
            s = "".join(map(str, file[0:index]))
        if s in d:
            tmp = False
            break
        else:
            d.add(s)
    index += 1
    find = tmp
print(index - 1)