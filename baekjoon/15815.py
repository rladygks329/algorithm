import sys

str = sys.stdin.readline().strip()

s = []
for ch in str:
    if '0' <= ch <= '9':
        s.append(int(ch))
        continue
    b, a = s.pop(), s.pop()
    if ch == '-':
        s.append(a-b)
    elif ch == '+':
        s.append(a+b)
    elif ch == '*':
        s.append(a*b)
    else:
        s.append(a//b)

print(s.pop())