import sys

stdin = sys.stdin.readline().strip()
answer = []
s = []

for ch in stdin:
    #operand
    if "A" <= ch <= "Z":
        answer.append(ch)
    #operator
    else:
        if not s:
            s.append(ch)
        else:
            if ch in "+-":
                while s and s[-1] != "(":
                    answer.append(s.pop())
                s.append(ch)
            elif ch in "*/":
                while s and s[-1] in "*/":
                    answer.append(s.pop())
                s.append(ch)
            elif ch == "(":
                s.append(ch)
            elif ch == ")":
                while s[-1] != "(":
                    answer.append(s.pop())
                s.pop()
while s:
    answer.append(s.pop())
print("".join(answer))