import sys

n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().rstrip()
    stack = []
    for j in s:
        if(j == "("):
            stack.append(j)
        elif(j == ")"):
            if(not stack):
                stack.append(j)
                break
            elif(stack[-1] != "("):
                break
            else:
                stack.pop()
    print("YES" if(not stack) else "NO")