#import sys
#sys.stdin = open("../input/2108.txt", "r")

import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    data.append(int(sys.stdin.readline()))

data.sort()
total = 0
high = -4001
low =  4001

count = 0
max_count = 0

once = True
often_value = data[0]
prev = data[0]

for i in data:
    total += i
    if(i < low):
        low = i
    if(i > high):
        high = i
    if(i == prev):
        count += 1
    else:
        if(count > max_count):
            max_count = count
            once = True
            often_value = prev
        elif(count == max_count):
            if(once):
                once = False
                often_value = prev
        count = 1
        prev = i
# 44444 일경우  44445 일경우 count = 1
if(count > max_count):
    max_count = count
    often_value = prev
elif(count == max_count):
    if(once):
        often_value = prev
print(round(total/n))
print(data[(n-1)//2])
print(often_value)
print(high - low)


