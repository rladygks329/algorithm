import sys

str = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
stack = []
index = 0

size1 = len(str)
size2 = len(bomb)

for ch in str:
    if ch == bomb[index]:
        index += 1
        stack.append((ch, index))
        if index == size2:
            for j in range(size2):
                stack.pop()
            index = stack[-1][1] if stack else 0
    else:
        index = 1 if ch == bomb[0] else 0
        stack.append((ch, index))

answer = "".join(list(map(lambda x: x[0], stack)))
print("FRULA" if answer == "" else answer)
