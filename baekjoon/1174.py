import sys

nth = int(sys.stdin.readline())
nth -= 1
arr = []
a = ""


# backtracking
def helper(s):
    for i in range(10):
        if s != "" and i >= int(s[-1]):
            break
        s += str(i)
        arr.append(int(s))
        helper(s)
        s = s.rstrip(s[-1])

helper(a)
arr.sort()
print(arr[nth] if nth < len(arr) else -1)
