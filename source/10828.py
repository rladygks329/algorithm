import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    input = sys.stdin.readline().rstrip()
    if(input == "pop"):
        if(not stack):
            print(-1)
        else:
            print(stack.pop())
    elif(input == "size"):
        print(len(stack))
    elif(input == "empty"):
        if(not stack):
            print(1)
        else:
            print(0)
    elif(input == "top"):
        if(not stack):
            print(-1)
        else:
            print(stack[-1])
    else:
        stack.append(int(input.split()[-1]))
