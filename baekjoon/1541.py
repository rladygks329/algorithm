import sys

def calc( s ):
    arr = s.split("+")
    result = 0
    for i in arr:
        result += int(i)
    return result

input = sys.stdin.readline()
data = input.split("-")

index = 0
answer = 0
while(index < len(data)):
    if(index == 0):
        answer += calc(data[index])
    else:
        answer -= calc(data[index])
    index += 1
print(answer)