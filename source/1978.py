import sys
#sys.stdin = open("../input/1978.txt", "r")

def sol(n):
    if(n == 1):
        return False
    if(n == 2):
        return True
    max = int(n ** 0.5)
    for i in range(2, max+1):
        if(n%i == 0):
            return False
    return True


n = int(input())
data = map(int, input().split())
count = 0

for i in data:
    if(sol(i)):
        count+=1
print(count)

