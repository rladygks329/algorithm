import sys

stdin = sys.stdin.read().splitlines()

N, M, B = map(int, stdin[0].split())
time = []
data = stdin[1::]
for i in range(len(data)):
    data[i] = list(map(int, data[i].split()))

for h in range(0, 257):
    t = 0
    b = B
    for i in data:
        for j in i:
            if(j > h):
                t += (j - h) * 2
                b += j-h
            elif(j < h):
                t += (h - j)
                b -= h-j
    if(b >= 0):
        time.append( (t, h) )
    if(time and t > time[-1][0]):
        break

time.sort(key= lambda answer: (answer[0], -answer[1]))
print(time[0][0], time[0][1])