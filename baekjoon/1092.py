import sys
from bisect import bisect_right

num_train = int(sys.stdin.readline())
trains = list(map(int, sys.stdin.readline().split()))
num_box = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))

trains.sort()
boxes.sort()

if trains[-1] < boxes[-1]:
    print(-1)
    sys.exit()

time = 0
while boxes:
    for train in trains:
        index = bisect_right(boxes, train)
        if index < len(boxes) and boxes[index-1] <= train:
            del boxes[index - 1]
        elif index == len(boxes):
            boxes.pop()
        if not boxes:
            break
    time += 1
print(time)
