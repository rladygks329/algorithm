import sys

def isBalance(s):
    stack = []

    for i in s:
        if(i == "(" or i == "["):
            stack.append(i)
        if( i == "]"):
            if(stack):
                if(stack[-1] == "["):
                    stack.pop()
                else:
                    print("no")
                    return
            else:
                print("no")
                return
        if (i == ")"):
            if (stack):
                if (stack[-1] == "("):
                    stack.pop()
                else:
                    print("no")
                    return
            else:
                print("no")
                return
    if(len(stack) == 0):
        print("yes")
    else:
        print("no")
    return

if __name__ == '__main__':
    while(True):
        s = sys.stdin.readline().rstrip()
        if(s == "."):
            break
        isBalance(s)